#!/usr/bin/env node
/** @file
    File name style checks.

    Copyright (C) 2020 by Christian Zuckschwerdt <zany@triq.net>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
*/

const { exec } = require("child_process")
const path = require('path')
const fs = require('fs')

const github = {
  sha: process.env.GITHUB_SHA,
  head_ref: process.env.GITHUB_HEAD_REF,
  base_ref: process.env.GITHUB_BASE_REF,
}

console.log(`sha: ${github.sha} head_ref: ${github.head_ref} base_ref: ${github.base_ref}`)
//const refspec = github.base_ref ? `${github.base_ref}..${github.head_ref}` : github.sha // would be master..master
//const refspec = github.base_ref ? `master..${github.sha}` : github.sha // unknown revision?
const refspec = github.sha
console.log(`refspec: ${refspec}`)

// Get a list of all files that have been changed.
// Ignore files that have been removed.
exec(`git diff-tree --no-commit-id --name-only -r ${refspec} --diff-filter d`, (error, stdout, stderr) => {
  if (error) {
    console.log(`::error::${error.message}`)
    process.exit(1)
  }
  if (stderr) {
    console.log(`::error::${stderr}`)
    process.exit(1)
  }
  //console.log(`stdout: ${stdout}`)

  const files = stdout.split('\n')
  let errors = 0
  let dirs_checked = []
  for (file of files) {
    const ext = path.extname(file)
    const dirname = path.dirname(file)
    const basename = path.basename(file)

    if (dirname.startsWith('tests/') && !dirs_checked.includes(dirname)) {
      if (!fs.existsSync(path.join(dirname, 'README.md'))) {
        console.log(`::error file=${file}::Add "README.md" to every dir level`)
        errors++
      }
      dirs_checked.push(dirname)
    }

    if (!file.startsWith('tests/')) {
      // not checked
    }
    else if (basename == 'ignore' || basename == 'protocol' || basename == 'samplerate') {
      // ok
    }
    else if (basename === 'README.md') {
      // ok
    }
    else if (dirname == 'tests') {
      console.log(`::error file=${file}::Don't add files to tests/ dir`)
      errors++
    }
    else if (ext.toLowerCase() != ext) {
      console.log(`::error file=${file}::Use lower-case extension`)
      errors++
    }
    else if (ext == '.jpeg') {
      console.log(`::error file=${file}::Use ".jpg" extension`)
      errors++
    }
    else if (file.indexOf(' ') >= 0) {
      console.log(`::error file=${file}::Don't use spaces in filenames`)
      errors++
    }
    else if (basename.toUpperCase().startsWith('README') && basename != 'README.md') {
      console.log(`::error file=${file}::Use "README.md" as filename`)
      errors++
    }
    else if (basename == 'codes_test.txt') {
      // codes_test.txt is consumed directly by bin/run_test.py and pairs with
      // codes_test.json in the same directory.
      // ok
    }
    else if (ext == '.txt') {
      console.log(`::warning file=${file}::Don't add random .txt files, use the README.md`)
    }
    else if (ext == '.md') {
      console.log(`::warning file=${file}::Don't add random .md files, use the README.md`)
    }
    else if (ext == '.json') {
      errors += check_json(file)
    }
    else if (ext == '.cu8') {
      errors += check_cu8(file)
    }
    else if (ext == '.cs8') {
      errors += check_cs8(file)
    }
    else if (ext == '.cs16') {
      errors += check_cs16(file)
    }
    else if (ext == '.jpg') {
      errors += check_image(file)
    }
    else if (ext == '.png') {
      errors += check_image(file)
    }
    else {
      console.log(`::error file=${file}::Don't add random files`)
      errors++
    }
  }

  process.exitCode = errors
})

function check_json(file) {
  const ext = path.extname(file)
  const dirname = path.dirname(file)
  const filename_no_ext = path.basename(file, ext)
  if (filename_no_ext === 'codes_test'
      && fs.existsSync(path.join(dirname, 'codes_test.txt'))) {
    return 0
  }
  if (!fs.existsSync(path.join(dirname, `${filename_no_ext}.cu8`))
      && !fs.existsSync(path.join(dirname, `${filename_no_ext}.cs8`))
      && !fs.existsSync(path.join(dirname, `${filename_no_ext}.cs16`))
      && !fs.existsSync(path.join(dirname, `${filename_no_ext}.ook`))) {
    console.log(`::error file=${file}::Add .json files only for .cu8/.cs8/.cs16/.ook files`)
    return 1
  }
  return 0
}

function check_max_size(file, max_size) {
  const stats = fs.statSync(file)
  if (stats.size > max_size) {
    console.log(`::error file=${file}::The file is too big, don't add raw captures`)
    return 1
  }
  return 0
}

function check_tags_present(file) {
  // check that frequency and samplerate tags are present...
  const freq_re = /\b[0-9]+\.?[0-9]*M\b/
  const rate_re = /\b[0-9]+\.?[0-9]*k\b/
  const file_split = file.replace(/[_-]/g, ' ')
  if (!file_split.match(freq_re) || !file_split.match(rate_re)) {
    console.log(`::error file=${file}::The file is missing meta data tags`)
    return 1
  }
  return 0
}

function check_cu8(file) {
  return check_max_size(file, 16 * 1024 * 1024) + check_tags_present(file)
}

function check_cs8(file) {
  return check_max_size(file, 8 * 1024 * 1024) + check_tags_present(file)
}

function check_cs16(file) {
  return check_max_size(file, 4 * 1024 * 1024) + check_tags_present(file)
}

function check_image(file) {
  // check:
  // _back.jpg
  // _front.jpg
  // _side.jpg
  // _battery.jpg
  // _inside.jpg
  // _inside_pcb.jpg
  // _sensor.jpg
  return 0
}

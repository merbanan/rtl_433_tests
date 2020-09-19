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
const refspec = github.base_ref ? 'master..${github.sha}' : github.sha
console.log(`refspec: ${refspec}`)

exec(`git diff-tree --no-commit-id --name-only -r ${refspec}`, (error, stdout, stderr) => {
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
    const dirname = path.basename(file)
    const basename = path.basename(file)
    const filename = path.basename(file, ext)

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
    else if (filename.toUpperCase().startsWith('README') && filename != 'README.md') {
      console.log(`::error file=${file}::Use "README.md" as filename`)
      errors++
    }
    else if (ext == '.txt') {
      console.log(`::warning file=${file}::foo Don't add random .txt files, use the README.md`)
    }
    else if (ext == '.md') {
      console.log(`::warning file=${file}::foo Don't add random .md files, use the README.md`)
    }
    else if (ext == '.json') {
      errors += check_json(file)
    }
    else if (ext == '.cu8') {
      errors += check_cu8(file)
    }
    else if (ext == '.jpg') {
      errors += check_image(file)
    }
    else if (ext == '.png') {
      errors += check_image(file)
    }
    else {
      console.log(`::error file=${file}::foo Don't add random files`)
      errors++
    }
  }

  process.exitCode = errors
})

function check_json(file) {
  const ext = path.extname(file)
  const dirname = path.basename(file)
  const filename = path.basename(file, ext)
  if (!fs.existsSync(path.join(dirname, filename, '.cu8'))) {
    console.log(`::error file=${file}::Add .json files only for .cu8 files`)
    return 1
  }
  return 0
}

function check_cu8(file) {
  const stats = fs.statSync(file)
  if (!stats.size > 1024*1024) {
    console.log(`::error file=${file}::The file is too big, don't add raw captures`)
    return 1
  }
  // check that frequency and samplerate tags are present...
  return 0
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

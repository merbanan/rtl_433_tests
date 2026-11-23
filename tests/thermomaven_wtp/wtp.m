
% ThermoMaven meat thermometer probe reverse engineering
%
% Copyright (C) 2026 Dan Dwyer
%
% This program is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 2 of the License, or
% (at your option) any later version.

clear all; close all; clc;

% This is a GNU Octave script used to characterize the Steinhart-Hart
% coefficients of the ThermoMaven WTP4000, WTP5000, and possibly other
% meat thermometer probes. Thermomaven is a wholly owned subsidiary of
% Typhur, Inc. and relevant FCC filings can be found at the following URL:
%   https://fcc.report/company/Typhur-Inc

% Columns in the following matrix correspond to internal temperatures 1-5
% followed by the ambient temperature. An example of what this looks like in the
% Thermomaven application is in wtp.png. Each row corresponds to what the app
% disclosed at a particular point in time, where the adjacent comment indicates
% the associated stimulus.
app_temps = [
  20.91 20.96 20.98 20.96 20.94 21.4       % probe 1 at ambient temperature
  20.73 20.76 20.75 20.76 20.75 21.0       % probe 2 ...
  101.42 100.20 100.28 100.39 100.69 100.4 % probe 1 at rolling boil
  102.39 100.83 100.67 100.61 100.89 101.0 % probe 2 ...
  2.30 1.71 1.41 1.34 1.12 0.2             % probe 1 in ice bath
  1.59 1.37 1.18 1.15 1.02 -0.3            % probe 2 ...
  31.84 34.08 36.41 36.90 38.93 145.2      % probe 1 w/ ~145C ambient
  31.84 34.08 36.41 36.90 38.93 145.2      % probe 1 w/ ~145C ambient
  31.84 34.08 36.41 36.90 38.93 145.2      % probe 1 w/ ~145C ambient
  31.97 34.27 36.65 37.19 39.45 153.3      % probe 2 w/ ~145C ambient
  31.97 34.27 36.65 37.19 39.45 153.3      % probe 2 w/ ~145C ambient
  31.97 34.27 36.65 37.19 39.45 153.3      % probe 2 w/ ~145C ambient
  31.97 34.27 36.65 37.19 39.45 153.3      % probe 2 w/ ~145C ambient
  58.90 60.12 61.66 61.93 63.01 119.5      % probe 1 at ~60C
  58.90 60.12 61.66 61.93 63.01 119.5      % probe 1 at ~60C
  58.90 60.12 61.66 61.93 63.01 119.5      % probe 1 at ~60C
  58.90 60.12 61.66 61.93 63.01 119.5      % probe 1 at ~60C
  58.94 60.29 61.74 62.10 63.36 119.5      % probe 2 at ~60C
  58.94 60.29 61.74 62.10 63.36 119.5      % probe 2 at ~60C
  58.94 60.29 61.74 62.10 63.36 119.5      % probe 2 at ~60C
  58.94 60.29 61.74 62.10 63.36 119.5      % probe 2 at ~60C
  72.80 73.26 73.75 73.74 74.08 150.1      % probe 1 at ~70C
  72.80 73.26 73.75 73.74 74.08 150.1      % probe 1 at ~70C
  72.80 73.26 73.75 73.74 74.08 150.1      % probe 1 at ~70C
  72.80 73.26 73.75 73.74 74.08 150.1      % probe 1 at ~70C
  73.02 73.45 73.91 74.05 74.32 154.8      % probe 2 at ~70C
  73.02 73.45 73.91 74.05 74.32 154.8      % probe 2 at ~70C
  73.02 73.45 73.91 74.05 74.32 154.8      % probe 2 at ~70C
  73.02 73.45 73.91 74.05 74.32 154.8      % probe 2 at ~70C
  73.02 73.45 73.91 74.05 74.32 154.8      % probe 2 at ~70C
  80.57 80.92 81.33 81.29 81.45 132.8      % probe 1 at ~80C
  80.57 80.92 81.33 81.29 81.45 132.8      % probe 1 at ~80C
  80.57 80.92 81.33 81.29 81.45 132.8      % probe 1 at ~80C
  80.57 80.92 81.33 81.29 81.45 132.8      % probe 1 at ~80C
  80.67 80.97 81.28 81.39 81.55 128.5      % probe 2 at ~80C
  80.67 80.97 81.28 81.39 81.55 128.5      % probe 2 at ~80C
  80.67 80.97 81.28 81.39 81.55 128.5      % probe 2 at ~80C
  80.67 80.97 81.28 81.39 81.55 128.5      % probe 2 at ~80C
  63.04 64.12 64.23 64.16 64.11 62.7       % probe 1 at ~60C (including ambient)
  62.77 64.14 64.15 64.19 64.19 61.8       % probe 2 at ~60C (including ambient)
  % Points that follow help to get additional coverage of the high temperature
  % stage of the ambient sensor. Other probe temperatures are zeroed out and
  % ignored in subsequent analysis.
  0 0 0 0 0 160.0
  0 0 0 0 0 160.0
  0 0 0 0 0 166.5
  0 0 0 0 0 166.5
  0 0 0 0 0 166.5
  0 0 0 0 0 172.7
  0 0 0 0 0 172.7
  0 0 0 0 0 172.7
  0 0 0 0 0 174.2
  0 0 0 0 0 174.2
  0 0 0 0 0 270.1
  0 0 0 0 0 270.1
  0 0 0 0 0 270.1
  0 0 0 0 0 308.5
  0 0 0 0 0 308.5
  0 0 0 0 0 386.2
  0 0 0 0 0 401.4
  0 0 0 0 0 401.4
  0 0 0 0 0 401.4
  0 0 0 0 0 420.5
  0 0 0 0 0 420.5
];

% Each row that follows is a codes excerpt that is similar to what is found in
% `codes_test.txt`, but excludes data up to the first temp probe and data that
% follows the battery codes. Each row is a radio sample that corresponds to the
% application observations in the preceding matrix.
raw_adc_codes = {
  '345611560756195619567b6f0d03'; % probe 1 at ambient temperature
  '7c565e56645660566456f66f0703';
  'e20d370e340e390e250e51110903'; % probe 1 at rolling boil
  '8a0df60d0d0e0b0ef30d1c11fd02';
  '4272b37210732c73727395890703'; % probe 1 in ice bath
  '1f731d734e7358738873148afa02';
  'dc45ae42953ff43e3a3cd6820a0b'; % probe 1 w/ ~145C ambient (g002_916M_1000k.cu8)
  'ce45a042733fdd3e283cd5820a0b'; % probe 1 w/ ~145C ambient (g003_916M_1000k.cu8)
  'a5457742413fb63ef73bb6820a0b'; % probe 1 w/ ~145C ambient (g005_916M_1000k.cu8)
  'cd459642583f9d3ea53be97c000b'; % probe 2 w/ ~145C ambient (g001_916M_1000k.cu8)
  'bf458242413f8f3e813bdf7c000b'; % probe 2 w/ ~145C ambient (g003_916M_1000k.cu8)
  'a8456042203f6b3e733bc67c000b'; % probe 2 w/ ~145C ambient (g004_916M_1000k.cu8)
  '96455242023f5d3e5c3bc17c000b'; % probe 2 w/ ~145C ambient (g005_916M_1000k.cu8)
  '3b26fc24a7236c2381229a0b0803'; % probe 1 at ~60C (g012_916M_1000k.cu8)
  '3126f2249d23622379229b0b0803'; % probe 1 at ~60C (g014_916M_1000k.cu8)
  '2726e7249323582377229c0b0903'; % probe 1 at ~60C (g016_916M_1000k.cu8)
  '1d26e5248923562376229e0b0903'; % probe 1 at ~60C (g018_916M_1000k.cu8)
  '3226da248d23442332229a0bfd02'; % probe 2 at ~60C (g009_916M_1000k.cu8)
  '2826cc248b233c233022a30bfd02'; % probe 2 at ~60C (g013_916M_1000k.cu8)
  '1e26c324822332232822ab0bfd02'; % probe 2 at ~60C (g015_916M_1000k.cu8)
  '1326c124782328231e22b30bfd02'; % probe 2 at ~60C (g017_916M_1000k.cu8)
  '471be41a911a8a1a4e1ac87c080b'; % probe 1 at ~70C (g020_916M_1000k.cu8)
  '451be21a891a801a4d1ac17c080b'; % probe 1 at ~70C (g022_916M_1000k.cu8)
  '3d1bd91a7f1a761a481ac17c080b'; % probe 1 at ~70C (g024_916M_1000k.cu8)
  '331bcf1a7d1a6c1a461ac67c080b'; % probe 1 at ~70C (g026_916M_1000k.cu8)
  '471be31a971a831a491af276fc0a'; % probe 2 at ~70C (g019_916M_1000k.cu8)
  '3f1bd81a8d1a741a471a2e77fd0a'; % probe 2 at ~70C (g021_916M_1000k.cu8)
  '351bce1a831a6b1a3f1a7477fc0a'; % probe 2 at ~70C (g023_916M_1000k.cu8)
  '331bcc1a811a691a351aba77fc0a'; % probe 2 at ~70C (g025_916M_1000k.cu8)
  '2a1bc41a6a1a681a331a1478fc0a'; % probe 2 at ~70C (g027_916M_1000k.cu8)
  'a6165e1626162b1615168286080b'; % probe 1 at ~80C (g028_916M_1000k.cu8)
  'a4165616251623160c168386080b'; % probe 1 at ~80C (g030_916M_1000k.cu8)
  '9c1654161d1621160a168286080b'; % probe 1 at ~80C (g032_916M_1000k.cu8)
  '9a164c161b16191609169886080b'; % probe 1 at ~80C (g034_916M_1000k.cu8)
  '9616561626161e1607166c88fc0a'; % probe 2 at ~80C (g029_916M_1000k.cu8)
  '94164e1624161616ff159088fc0a'; % probe 2 at ~80C (g031_916M_1000k.cu8)
  '7f1644161c161416fd158288fc0a'; % probe 2 at ~80C (g033_916M_1000k.cu8)
  '7e1642161a161316fc158888fc0a'; % probe 2 at ~80C (g035_916M_1000k.cu8)
  'a8229321862194219721c5300403'; % probe 1 at ~60C (including ambient)
  'c622802185217a2182216c31f902'; % probe 2 at ~60C (including ambient)
  '99577d57825776575e57c67ae70a'; % 160.0C Ambient
  '995780577e5777575d57947ae70a'; % 160.0C Ambient
  '935779577d57765757576c75e70a'; % 166.5C Ambient
  '945779577c57755757574475e70a'; % 166.5C Ambient
  '945779577b5774575757f474e70a'; % 166.5C Ambient
  '92577457715768574757096ce70a'; % 172.7C Ambient
  '91577357705768574757e46be70a'; % 172.7C Ambient
  '935773576f5768574757e06be70a'; % 172.7C Ambient
  '9457785774576c574c574c6de70a'; % 174.2C Ambient
  '9457785774576d574b573e6de70a'; % 174.2C Ambient
  '8f576b5764575a573357882ce70a'; % 270.1C Ambient
  '8f576d5764575a572f57002de70a'; % 270.1C Ambient
  '8f576e57645758572f576e2de70a'; % 270.1C Ambient
  '855755573c573057dc56861ae70a'; % 308.5C Ambient
  '855755573c572f57db56e41be70a'; % 308.5C Ambient
  '85575a5746573757ed56a80ce70a'; % 386.2C Ambient
  '85575a5746573857f056280ae70a'; % 401.4C Ambient
  '85575a5746573757ef56be0ae70a'; % 401.4C Ambient
  '85575a5746573757ee564a0be70a'; % 401.4C Ambient
  '85575f574a574057fb569006e70a'; % 420.5C Ambient
  '85575f5749574057fa56b806e70a'; % 420.5C Ambient
};

% Parse bytes into a 12x6 matrix (each column is one string's 12 bytes), then transpose to 6x12
bytes = reshape(uint16(sscanf(strjoin(raw_adc_codes, ''), '%2x')), 14, []).';

% Combine odd columns (LSB) and even columns (MSB) mathematically
adc_matrix = double(bitor(bytes(:, 1:2:end), bitshift(bytes(:, 2:2:end), 8)));

% The battery ADC value uses 10-bits out of the 16-bit field. The
% preceding 11th bit is a flag that indicates which of two gain
% stages is used for the ambient temperature sensor.
adc_battery = adc_matrix(:,end);
adc_matrix = adc_matrix(:,1:end-1);
adc_flag_set = bitand(adc_battery, 0x0800) != 0;
adc_battery = bitand(adc_battery, 0x07ff);

% Get X matrix to help w/ coefficient fit of
%   https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation
function [X] = get_x(d_max, adc)
  r = adc ./ (d_max - adc);
  L = log(r);
  X = [ones(size(r)), L, L.^2, L.^3];
end

% Single-group evaluation function
function [rmse, coeffs] = single_eval(d_max, adc, T)
  X = get_x(d_max, adc);
  coeffs = X \ (1 ./ (T + 273.15));
  err = ((1 ./ (X * coeffs)) - 273.15) - T;
  rmse = sqrt(mean(err.^2));
  % rmse = max(abs(err));
  if (d_max < (max(adc)-1))
    rmse = Inf;
  endif
end

% Helper wrapper for grid sweep + fminbnd refinement
function [d_best, rmse_best, coeffs_best, d_grid, rmse_vec] = find_best_dmax(adc, T, d_upper)
  d_min = ceil(max(adc(:))/5)*5;
  d_grid = d_min : 5 : d_upper;
  rmse_vec = arrayfun(@(d) single_eval(d, adc, T), d_grid);

  [~, idx] = min(rmse_vec);
  d_coarse = d_grid(idx);

  % Refine within +/- 200 counts of the grid winner
  opts = optimset('TolX', 1e-4);
  d_best = fminbnd(@(d) single_eval(d, adc, T), ...
                   max(max(adc(:)) + 1, d_coarse - 200), d_coarse + 200, opts);
  [rmse_best, coeffs_best] = single_eval(d_best, adc, T);
end

function print_fit(adc_cal, T_c, title_substring)
  % Search for optimal D_max between max(adc_cal)+1 and 100000
  lower_bound = max(adc_cal) + 1;
  upper_bound = 100000;

  opts = optimset('MaxIter', 1000, ...
                  'MaxFunEvals', 2000, ...
                  %'TolX', 1e-3, ... % Stop when D_max is within 0.001 counts
                  'Display', 'off'); % Print iteration progress (use 'off' to silence)


  D_max_opt = fminbnd(@(d) single_eval(d, adc_cal, T_c), lower_bound, upper_bound, opts);

  % Recover the final [A'; B'; C'] coefficients at D_max_opt
  [~, coeffs_opt] = single_eval(D_max_opt, adc_cal, T_c);
  fprintf('Estimated D_max: %.2f\n', D_max_opt);

  X = get_x(D_max_opt,adc_cal);

  T_meas = ((X * coeffs_opt).^(-1))-273.15;
  err = T_meas - T_c;
  max_abs_err = max(abs(err))

  x = linspace(min(adc_cal),max(adc_cal),1000);
  x = x';
  X = get_x(D_max_opt,x);
  adc_meas = ((X * coeffs_opt).^(-1))-273.15;
  figure, plot(adc_cal,T_c,'*',x,adc_meas,'.-');
  xlabel('ADC Value (counts)');
  ylabel('Temperature (°C)');
  title(sprintf('ADC to Temperature Transfer Function\n(%s)',title_substring));
  legend('Recorded Values','Interpolated Values');
  grid on;
end

function [rmse, coeffs] = eval_fit(d_max, adc, T_c, therm_on_top)
  X = get_x(d_max, adc);
  y = 1 ./ (T_c + 273.15);
  coeffs = X \ y;
  T_pred = (1 ./ (X * coeffs)) - 273.15;
  rmse = sqrt(mean((T_c - T_pred).^2));
end

% Internal 1-5
adc_meat = reshape(adc_matrix(1:40, 1:5), [], 1);
T_meat   = reshape(app_temps(1:40, 1:5), [], 1);
print_fit(adc_meat,T_meat,'Internal');
saveas(gcf,'internal','png');

% Ambient Low Temp
adc_amb_lo = adc_matrix(~adc_flag_set,end);
T_amb_lo   = app_temps(~adc_flag_set,end);
print_fit(adc_amb_lo,T_amb_lo, 'Ambient Low Temperature');
saveas(gcf,'ambient_low','png');

% Ambient High Temp
adc_amb_hi = adc_matrix(adc_flag_set,end);
T_amb_hi     = app_temps(adc_flag_set,end);
print_fit(adc_amb_hi,T_amb_hi, 'Ambient High Temperature');
saveas(gcf,'ambient_high','png');

% 1. Run independent exhaustive searches for optimal D-max values (up to 100,000)
[d_meat, rmse_meat, c_meat, grid_m, vec_m] = find_best_dmax(adc_meat, T_meat, 100000);
[d_amb_lo,  rmse_amb_lo,  c_amb_lo, grid_a_lo, vec_a_lo] = find_best_dmax(adc_amb_lo, T_amb_lo, 100000);
[d_amb_hi,  rmse_amb_hi,  c_amb_hi, grid_a_hi, vec_a_hi] = find_best_dmax(adc_amb_hi, T_amb_hi, 100000);

% 2. Print out the associated optimal D-max values and Steinhart Hart coefficients
fprintf('MEAT (Ch 1-5)  | D_max = %8.2f | RMSE = %.4f C | A=%.8e, B=%.8e, C=%.8e, D=%.8e\n', ...
        d_meat, rmse_meat, c_meat);
fprintf('AMB  (Ch 6/Lo) | D_max = %8.2f | RMSE = %.4f C | A=%.8e, B=%.8e, C=%.8e, D=%.8e\n', ...
        d_amb_lo, rmse_amb_lo, c_amb_lo);
fprintf('AMB  (Ch 6/Hi) | D_max = %8.2f | RMSE = %.4f C | A=%.8e, B=%.8e, C=%.8e, D=%.8e\n', ...
        d_amb_hi, rmse_amb_hi, c_amb_hi);

% 3. Plot root mean squared error as a function of D-max
figure;
plot(grid_m, vec_m, 'b-', 'LineWidth', 1.5, ...
     grid_a_lo, vec_a_lo, 'r-', 'LineWidth', 1.5, ...
     grid_a_hi, vec_a_hi, 'g-', 'LineWidth', 1.5);
xlabel('Candidate D_{max}');
ylabel('RMSE (°C)');
title('Independent D_{max} Error Landscapes');
legend('Meat Channels (1-5)', 'Ambient Channel Lo (6)', 'Ambient Channel Hi (6)');
grid on;
saveas(gcf,'d_max_error','png');


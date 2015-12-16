set term postscript eps size 3.5,2.62 font 'Times, 20
set output 'img_rho_R.eps'

set xlabel 'Budget'
set ylabel 'Budget utilization ratio'

set xrange [0:11000]
set key off
set boxwidth 800
set style line 1 lc rgb "blue" lw 3
set style fill solid 0.3 
plot 'rho_R.txt' using 1:2:3  w boxerror ls 1

set term x11
set output

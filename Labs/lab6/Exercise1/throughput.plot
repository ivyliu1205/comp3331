set xlabel "time [s]"
set ylabel "Throughput [Mbps]"
set key bel
plot "tcp1.tr" u ($1):($2) t "TCP1" w lp lt rgb "blue", "tcp2.tr" u ($1):($2) t "TCP2" w lp lt 1 pt 2


set term png
set output "exercise1_plot.png" 
replot
pause -1

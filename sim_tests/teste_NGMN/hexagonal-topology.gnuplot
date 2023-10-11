set term pdf
set output "./hexagonal-topology.gnuplot.pdf"
set style arrow 1 lc "black" lt 1 head filled
set xrange [-2001:2001]
set yrange [-2001:2001]
set arrow 1 from 0,0 rto 36.0844,20.8333 arrowstyle 1 
set object 1 polygon from \
145.204, -82.8333 to \
0.866025, 0.5 to \
0.866025, 167.167 to \
145.204, 250.5 to \
289.541, 167.167 to \
289.541, 0.5 to \
145.204, -82.8333 front fs empty 
set label 1 "1" at 145.204 , 83.8333 center
set arrow 2 from 0,0 rto -36.0844,20.8333 arrowstyle 1 
set object 2 polygon from \
-145.204, -82.8333 to \
-289.541, 0.5 to \
-289.541, 167.167 to \
-145.204, 250.5 to \
-0.866025, 167.167 to \
-0.866025, 0.5 to \
-145.204, -82.8333 front fs empty 
set label 2 "2" at -145.204 , 83.8333 center
set arrow 3 from 0,0 rto -7.65404e-15,-41.6667 arrowstyle 1 
set object 3 polygon from \
-1.83697e-16, -334.333 to \
-144.338, -251 to \
-144.338, -84.3333 to \
-1.83697e-16, -1 to \
144.338, -84.3333 to \
144.338, -251 to \
-1.83697e-16, -334.333 front fs empty 
set label 3 "3" at -1.83697e-16 , -167.667 center
set label at 185.058 , 189.149 point pointtype 7 pointsize 0.2 center
set label at -168.921 , 193.54 point pointtype 7 pointsize 0.2 center
set label at 97.048 , -209.978 point pointtype 7 pointsize 0.2 center
set label at 175.986 , -39.5368 point pointtype 7 pointsize 0.2 center
set label at -51.4754 , 63.2972 point pointtype 7 pointsize 0.2 center
set label at -28.0851 , -212.021 point pointtype 7 pointsize 0.2 center
set label at 190.279 , 63.4254 point pointtype 7 pointsize 0.2 center
set label at -157.91 , 23.9708 point pointtype 7 pointsize 0.2 center
set label at -21.0854 , -120.999 point pointtype 7 pointsize 0.2 center
set label at 159.46 , 130.302 point pointtype 7 pointsize 0.2 center
set label at -192.665 , 142.572 point pointtype 7 pointsize 0.2 center
set label at 74.7687 , -96.5661 point pointtype 7 pointsize 0.2 center
set label at 111.246 , 203.068 point pointtype 7 pointsize 0.2 center
set label at -101.184 , 130.125 point pointtype 7 pointsize 0.2 center
set label at 30.5465 , -208.492 point pointtype 7 pointsize 0.2 center
set label at 216.538 , 62.0085 point pointtype 7 pointsize 0.2 center
set label at -174.437 , 103.258 point pointtype 7 pointsize 0.2 center
set label at -15.373 , -87.6712 point pointtype 7 pointsize 0.2 center
set label at 146.974 , 209.669 point pointtype 7 pointsize 0.2 center
set label at -187.099 , 202.809 point pointtype 7 pointsize 0.2 center
set label at -62.0073 , -216.496 point pointtype 7 pointsize 0.2 center
set label at 160.102 , 116.18 point pointtype 7 pointsize 0.2 center
set label at -203.843 , 201.885 point pointtype 7 pointsize 0.2 center
set label at -101.818 , -111.066 point pointtype 7 pointsize 0.2 center
set label at 175.239 , -0.188219 point pointtype 7 pointsize 0.2 center
set label at -168.196 , 9.40391 point pointtype 7 pointsize 0.2 center
set label at 116.879 , -129.148 point pointtype 7 pointsize 0.2 center
set label at 132.752 , 152.716 point pointtype 7 pointsize 0.2 center
set label at -101.75 , 32.1819 point pointtype 7 pointsize 0.2 center
set label at -17.4255 , -290.592 point pointtype 7 pointsize 0.2 center
unset key
plot 1/0

clear
close all
clc

s = load('ecg.txt');
fs = 250;
fc = 60;
n = 6;
Wn = fc/(fs/2);
[b,a]=butter(n,Wn,'low');
freqz(b,a)
sf2=filter(b,a,s);
subplot(211)
plot(s)
subplot(212)
plot(sf2)
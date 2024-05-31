FROM ubuntu:18.04
MAINTAINER Radoslaw 'radon' Zdonczyk "rzdonczyk@trustwave.com" 
# Spiderlabs Research - Database Security Team
# Squirell for SQLite3 fuzz image

# Prerequisites
ENV TERM=xterm
RUN ln -fs /usr/share/zoneinfo/UTC /etc/localtime
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install apt-utils tcl pkg-config gdb bison flex git \
	make cmake build-essential gcc-multilib g++-multilib xinetd \
	libreadline-dev zlib1g-dev clang libssl-dev wget && \
	apt-get autoremove -y && apt-get autoclean -y

### BUILD & FUZZ 

WORKDIR /home/fuzz

## AFL
RUN git clone https://github.com/google/AFL.git
WORKDIR /home/fuzz/AFL 
RUN sed -i  's/#define MAP_SIZE_POW2       16/#define MAP_SIZE_POW2       18/' config.h
RUN make
WORKDIR /home/fuzz/AFL/llvm_mode
ENV LLVM_CONFIG=llvm-config-6.0
RUN make 

## Squirell
WORKDIR /home/fuzz
RUN git clone https://github.com/s3team/Squirrel.git
WORKDIR /home/fuzz/Squirrel/SQLite/AFL
RUN make afl-fuzz

## SQLite3
WORKDIR /home/fuzz
RUN rm -rf /home/fuzz/sqlite \
	&& wget -O sqlite.tar.gz https://www.sqlite.org/src/tarball/sqlite.tar.gz?r=release \
	&& tar xvfz sqlite.tar.gz

# AFL instrumentation
ENV AFL_HARDEN=1
ENV CC=/home/fuzz/AFL/afl-clang
ENV CXX=/home/fuzz/AFL/afl-clang++

# AFL build
WORKDIR /home/fuzz/sqlite/bld
RUN ../configure --disable-shared && make -j`nproc`

# Squirell fuzz
WORKDIR /home/fuzz/Squirrel/SQLite/fuzz_root
RUN mkdir output

CMD ../AFL/afl-fuzz -i input/ -o output/ -f log.log -- ../../../sqlite/bld/sqlite3 --bail

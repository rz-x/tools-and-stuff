

- fuzz start:

container_home_fuzz_seeds_1: docker run -d --memory="1g" --memory-swap="1.8g" --cpus="1" -v /root/squirell_sqlite3/container_home_fuzz_seeds_1/fuzz_root:/home/fuzz/Squirrel/SQLite/fuzz_root fuzz_sqlite:latest 

container_home_fuzz_seeds_2: docker run -d --memory="1g" --memory-swap="2g" --cpus="1" -v /root/squirell_sqlite3/container_home_fuzz_seeds_2/fuzz_root:/home/fuzz/Squirrel/SQLite/fuzz_root fuzz_sqlite:latest  
import subprocess
import concurrent.futures

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.submit(subprocess.run, ['scrapy', 'crawl', 'amazon_sa', '-o', 'amazon_sa.json'])
        executor.submit(subprocess.run, ['scrapy', 'crawl', 'firstcry_sa', '-o', 'firstcry_sa.json'])
        executor.submit(subprocess.run, ['scrapy', 'crawl', 'firstcry_ae', '-o', 'firstcry_ae.json'])
        executor.submit(subprocess.run, ['scrapy', 'crawl', 'noon_com', '-o', 'noon_com.json'])
        executor.submit(subprocess.run, ['scrapy', 'crawl', 'noon_saudien', '-o', 'noon_saudien.json'])
        executor.submit(subprocess.run, ['scrapy', 'crawl', 'amazon_ae', '-o', 'amazon_ae.json'])
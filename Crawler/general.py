import os
#every website you crawl is a new project
def create_proj_dir(directory):
    if not os.path.exists(directory):
        print("Creating new project " + directory)
        os.makedirs(directory)


#create_proj_dir('testingOne')


#create Queue and Crawled files
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')


#create  a file
def write_file(path,data):
    f = open(path,'w')
    f.write(data)
    f.close()


#create_data_files('testingOne','https://thenewboston.com/')

#add data onto an existing file
def append_to_file(path,data):
    with open(path,'a') as file :
        file.write(data + '\n')

#delete the contents of a file
def delete_file_contents(path):
    with open(path,'w'):
        pass

#Read a file a convert to set item
def file_to_set(file_name):
    results = set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

#Iterate through a set , each item will be  a line in the file
def set_to_file(links,file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file,link)





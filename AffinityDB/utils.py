import os
import sys
import config

def mkdir(path):
    # make directory recursive, doesn't have warry info when path exists
    os.system('mkdir -p {}'.format(path))


def log(log_file, log_content, head=None, lock=None):
    """
    write down log information
    :param log_file: name of log file
    :param log_content: string or list of string, log content
    :param head: head for csv or tsv output file
    :param lock: multiprocess lock
    :return: 
    """

    lock.acquire()

    if isinstance(log_content, str):
        log_content = [log_content]

    mkdir(config.log_folder)

    log_file_path = os.path.join(config.log_folder, log_file)
    if not os.path.exists(log_file_path) and not head is None:
        with open(log_file_path, 'w') as fout:
            fout.write(head+'\n')
    with open(log_file_path, 'a') as fout:
        for cont in log_content:
            fout.write(cont+'\n')

    lock.release()
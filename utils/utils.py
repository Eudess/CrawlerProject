import re

def is_npu(npu):
    clean_number = clean_npu(npu)
    return len(clean_number) == 20


def formatter_npu(npu):
    npu_clean = clean_npu(npu)
    formatted_npu = f"{npu_clean[:7]}-{npu_clean[7:9]}.{npu_clean[9:13]}.{npu_clean[13:14]}.{npu_clean[14:]}"
    return formatted_npu


def clean_npu(npu):
    regex = r'\d+'
    numbers = re.findall(regex, npu)
    return "".join(numbers)
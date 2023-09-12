# 导入LangChain中的提示模板
from langchain import PromptTemplate
# 创建原始模板
template = """You are a flower shop assitiant。\n
For {price} of {flower_name} ，can you write something for me？
"""
# 根据原始模板创建LangChain提示模板
prompt = PromptTemplate.from_template(template) 
# 打印LangChain提示模板的内容
print(prompt)

# 设置HuggingFace API Token
import os
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '你的HUGGINGFACEHUB API Token'

# 导入LangChain中的OpenAI模型接口
from langchain import HuggingFaceHub
# 创建模型实例
model= HuggingFaceHub(repo_id="google/flan-t5-large")
# 输入提示
input = prompt.format(flower_name=["玫瑰"], price='50')
# 得到模型的输出
output = model(input)
# 打印输出内容
print(output)

from openai import OpenAI 
from .prompts import sys_prompt, sys_img_prompt

class PostGenerator:
    def __init__(self, openai_key, tone, topic, sys_prompt = sys_prompt):
        self.client = OpenAI(api_key=openai_key)
        self.tone = tone
        self.topic = topic 
        self.sys_prompt = sys_prompt
        self.user_prompt = f"Создай пост для соцсетей с темой: {topic}, используя тон: {tone}"


    def generate_post(self):
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": self.sys_prompt},
                {"role": "user", "content": self.user_prompt}
            ]
        )
        return response.choices[0].message.content

    def generate_post_image_description(self, sys_img_prompt = sys_img_prompt):
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": sys_img_prompt},
                {"role": "user", "content": f"Напиши промпт для генерации изображения на тему {self.topic}"}
            ]
        )
        return response.choices[0].message.content
    
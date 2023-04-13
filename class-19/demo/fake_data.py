import os
import shutil

from faker import Faker

fake = Faker('en_US')

# print(dir(fake))

fake_words = fake.words()
# print(fake_words)

fake_sentence = fake.sentence()
# print(fake_sentence)

fake_email = fake.email()
# print(fake_email)

fake_paragraph = fake.paragraph(4)

fake_phone = fake.phone_number()
for _ in range(100):
    fake_words = fake.words()
    # print(fake_words)

# print(fake_paragraph)
# print(fake_email)
# print(fake_phone)
content = ''
for _ in range(100):

    content += fake.paragraph(3)
    content += fake.email()
    content += fake.phone_number()
    content += fake.paragraph(2)
    # print(content)

    with open('content.txt', 'w+') as f:
        f.write(content)
os.mkdir('assets',)
shutil.copy('content.txt', './assets')

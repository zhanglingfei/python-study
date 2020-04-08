orig_sentence='and hence should not be used for determining accurate long-term trajectories trajectories，and hence should not be used for determining accurate long-term trajectories trajectoriesand ' \
              'hence should not be used for determining accurate long-term trajectories trajectoriesand hence should not be used for determining accurate long-term trajectories trajectoriesand ' \
              'hence should not be used for determining accurate long-term trajectories trajectoriesand hence should not be used for determining accurate long-term trajectories trajectoriesand ' \
              'hence should not be used for determining accurate long-term trajectories trajectoriesand ' \
              'hence should not be used for determining accurate long-term trajectories trajectoriesand hence should not be used for determining accurate long-term trajectories trajectories'
print(len(orig_sentence))
import re

def cut_text(text, lenth):
    textArr = re.findall('.{' + str(lenth) + '}', text)
    body_text=text[(len(textArr) * lenth):]

    textArr.append(body_text)
    return textArr


text_list=cut_text(f'{orig_sentence}', 89)
final_text=''
for text in text_list:
    final_text+=f'{text}\\n'

print(final_text)

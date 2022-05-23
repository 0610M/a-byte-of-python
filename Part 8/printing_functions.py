# 定义一个函数print_model()打印模型，将列表unprinted_designs和completed_models
# 存储在print_model函数中
def print_model(unprinted_designs, completed_models):
    """使用while循环查找没有打印的列表unprinted_designs"""
    while unprinted_designs:
        # 将unprinted_designs列表中末尾的值取出存储在current_design变量中
        current_design = unprinted_designs.pop()
        # 显示循环中打印的数值模型
        print("打印正在进行" + current_design)
        # 将已经打印好的模型，存放到completed_models的列表中去
        completed_models.append(current_design)


# 定义x_models()函数已经打印模型，把已经打印的completed_models列表存储在函数中
def x_models(completed_models):
    # 打印显示打印模型文字提示
    print("显示打印模型：")
    # 使用for 函数遍历列表中的x_model,并打印出来
    for x_model in completed_models:
        # 打印处理x_model 的值
        print(x_model)

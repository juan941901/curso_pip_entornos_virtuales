import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'c']
    values = [22, 35, 12]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png') #
    plt.close()

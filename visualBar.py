import matplotlib.pyplot as plt

def graphCityStats(name, subject, polar):
    ax = plt.subplot(111)
    index = range(len(name))
    x1 = [index - .1 for index in index]
    x2 = [index + .1 for index in index]
    polarity = ax.bar(x1, subject, width=.2, color='r', align='center')
    subjectivity = ax.bar(x2, polar, width=.2,color='g', align='center')
    plt.xlabel('Cities')
    plt.ylabel('Urgency Score')
    plt.xticks(index, name, rotation=45)
    plt.title('Assistance Urgency')
    plt.legend([polarity, subjectivity], ['Crisis Level', 'Info. Reliability'])
    plt.subplots_adjust(bottom=.25)
    plt.show()

if __name__ == "__main__":
    polar = [5,3,9,10,25,3,7,12]
    subject = [2,5,4,4,7,10,18,1]
    name = ['Amarillo', 'Austin', 'Dallas', 'El Paso', 'Houston', 'San Antonio', 'Shit Stain', 'Waco']
    graphCityStats(name, subject, polar)

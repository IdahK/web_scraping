from bs4 import BeautifulSoup
import requests

def scrape():
    #Find instances of tags
    l = []
    url = 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'
    result = requests.get(url)
    extra_data = {}
    paragraph_data =  { }
    response_object = result # response object
    status_code = result.status_code
    result_text = result.text
    soup = BeautifulSoup(result.text,'html.parser')
    paragraph_elements = soup.find_all('p') #instances of <p> tag
   

    for item in paragraph_elements:
        paragraph_data[str(item.get('id'))]=  str(item)
    # chorus_elements = soup.find_all(class_='chorus') #finding instances of the class chorus
    # chorus_paragraphs = soup.find_all('p',class_='chorus') #find instances of <p> of the class chorus
    # third_id_elements = soup.find_all(id= 'third')  # find instances of id third
    
    extra_data['status_code'] = status_code
    extra_data['result_text'] = result_text

    l.append(paragraph_data)
    l.append(extra_data)
    return l

if __name__ == "__main__":
    print(scrape())  
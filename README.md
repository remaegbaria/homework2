# homework2

Python Code that receives a country name and it returns Country’s Full Name Capital Common Language Currency Name and Currency rate.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install:

```bash
pip install flask
pip install requests
```

## To run the code (server)

```bash
git clone https://github.com/remaegbaria/homework2.git
cd homework2
python app.py
```

## open another command line(client)

```bash
curl http://127.0.0.1:5000/Users/%22rema%20egbaria%22/Desktop/aruba
```

## To create image and run with Docker

```bash
docker build -t homework2 .
docker run -i -t -d -p 5000:5000 homework2
curl http://127.0.0.1:5000/Users/%22rema%20egbaria%22/Desktop/aruba
```


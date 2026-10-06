{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "37290250-0cb7-405a-b5fd-d0c0a5c6b538",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (1.51.0)\n",
      "Requirement already satisfied: altair!=5.4.0,!=5.4.1,<6,>=4.0 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from streamlit) (5.5.0)\n",
      "Requirement already satisfied: blinker<2,>=1.5.0 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from streamlit) (1.9.0)\n",
      "Requirement already satisfied: cachetools<7,>=4.0 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from streamlit) (5.5.1)\n",
      "Requirement already satisfied: click<9,>=7.0 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from streamlit) (8.2.1)\n",
      "Requirement already satisfied: numpy<3,>=1.23 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from streamlit) (2.3.5)\n",
      "Requirement already satisfied: packaging<26,>=20 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from streamlit) (25.0)\n",
      "Requirement already satisfied: pandas<3,>=1.4.0 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from streamlit) (2.3.3)\n",
      "Requirement already satisfied: pillow<13,>=7.1.0 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from streamlit) (12.0.0)\n",
      "Collecting protobuf<7,>=3.20 (from streamlit)\n",
      "  Downloading protobuf-6.33.6-cp310-abi3-win_amd64.whl.metadata (593 bytes)\n",
      "Requirement already satisfied: pyarrow<22,>=7.0 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from streamlit) (21.0.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from streamlit) (2.32.5)\n",
      "Requirement already satisfied: tenacity<10,>=8.1.0 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from streamlit) (9.1.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.4.0 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from streamlit) (4.15.0)\n",
      "Requirement already satisfied: watchdog<7,>=2.1.5 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from streamlit) (6.0.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from streamlit) (3.1.45)\n",
      "Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from streamlit) (6.5.1)\n",
      "Requirement already satisfied: jinja2 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.1.6)\n",
      "Requirement already satisfied: jsonschema>=3.0 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (4.25.0)\n",
      "Requirement already satisfied: narwhals>=1.14.2 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2.7.0)\n",
      "Requirement already satisfied: colorama in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
      "Requirement already satisfied: tzdata>=2022.7 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
      "Requirement already satisfied: charset_normalizer<4,>=2 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.4.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.11)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.5.0)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2025.11.12)\n",
      "Requirement already satisfied: attrs>=22.2.0 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (25.4.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2025.9.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.37.0)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.28.0)\n",
      "Requirement already satisfied: six>=1.5 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in d:\\users\\priyanshu chaudhary\\anaconda3\\lib\\site-packages (from jinja2->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.0.2)\n",
      "Downloading protobuf-6.33.6-cp310-abi3-win_amd64.whl (437 kB)\n",
      "Installing collected packages: protobuf\n",
      "  Attempting uninstall: protobuf\n",
      "    Found existing installation: protobuf 7.36.2\n",
      "    Uninstalling protobuf-7.36.2:\n",
      "      Successfully uninstalled protobuf-7.36.2\n",
      "Successfully installed protobuf-6.33.6\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "  WARNING: Failed to remove contents in a temporary directory 'D:\\Users\\PRIYANSHU CHAUDHARY\\anaconda3\\Lib\\site-packages\\google\\~upb'.\n",
      "  You can safely remove it manually.\n"
     ]
    }
   ],
   "source": [
    "%pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e4dbbb41-6922-461f-8811-ef1e5cae4d4b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "import tensorflow as tf\n",
    "from sklearn.preprocessing import StandardScaler , LabelEncoder , OneHotEncoder\n",
    "import pandas as pd\n",
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "60f478f9-b178-44c5-86b2-0f3f04b8032e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WARNING:tensorflow:TensorFlow GPU support is not available on native Windows for TensorFlow >= 2.11. Even if CUDA/cuDNN are installed, GPU will not be used. Please use WSL2 or the TensorFlow-DirectML plugin.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING:absl:Compiled the loaded model, but the compiled metrics have yet to be built. `model.compile_metrics` will be empty until you train or evaluate the model.\n"
     ]
    }
   ],
   "source": [
    "model = tf.keras.models.load_model(\"model.h5\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f3e2b7df-08be-4427-960e-9555340e6b1b",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('label_encoder_gender.pkl','rb') as file:\n",
    "    lebel_encoder_gender = pickle.load(file)\n",
    "\n",
    "with open('ohe_geo.pkl','rb') as file:\n",
    "    ohe_geo = pickle.load(file)\n",
    "\n",
    "with open('scaler.pkl','rb') as file:\n",
    "    scaler = pickle.load(file)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f3a4cffe-8f33-4cb7-a614-457d0daac0d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-09-28 18:24:33.090 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:24:36.652 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run D:\\Users\\PRIYANSHU CHAUDHARY\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2026-09-28 18:24:36.653 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:24:36.660 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.title('customer Churn Prediction')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "97a76db8-8d9e-40c0-a083-46a685f31487",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-09-28 18:27:55.383 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.385 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.390 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.392 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.394 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.396 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.398 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.399 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.401 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.402 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.404 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.405 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.406 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.408 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.409 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.410 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.411 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.412 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.414 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.415 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.416 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.416 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.417 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.418 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.419 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.421 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.422 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.423 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.424 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.425 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.426 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.427 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.429 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.430 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.433 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.434 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.436 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.439 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.441 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.443 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.444 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.445 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.447 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.448 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.449 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.450 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.451 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.452 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.453 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.454 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.455 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.457 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.459 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.460 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.461 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.464 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.466 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.468 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.470 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.471 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.474 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.477 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.477 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.479 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.485 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.487 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.488 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.490 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.492 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-28 18:27:55.496 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "# User input\n",
    "geography = st.selectbox('Geography', ohe_geo.categories_[0])\n",
    "gender = st.selectbox('Gender', ['Male', 'Female'])\n",
    "age = st.slider('Age', 18, 92)\n",
    "balance = st.number_input('Balance')\n",
    "credit_score = st.number_input('Credit Score')\n",
    "estimated_salary = st.number_input('Estimated Salary')\n",
    "tenure = st.slider('Tenure', 0, 10)\n",
    "num_of_products = st.slider('Number of Products', 1, 4)\n",
    "has_cr_card = st.selectbox('Has Credit Card', [0, 1])\n",
    "is_active_member = st.selectbox('Is Active Member', [0, 1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "26291c1b-59f9-48c4-ac78-8089732c9e10",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

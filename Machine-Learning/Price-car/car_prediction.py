{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Predicting used car prices\n",
    "\n",
    "In this notebook, I'll work with the [Kaggle](https://www.kaggle.com/avikasliwal/used-cars-price-prediction) dataset about used cars and their prices. The notebook first includes exploration of the dataset followed by prediction of prices."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Import libraries\n",
    "\n",
    "I'll import `datetime` to handle year, `numpy` to work with arrays and `pandas` to read in the dataset files, `matplotlib` & `seaborn` for plotting and `sklearn` for various machine learning models."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime\n",
    "\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "%matplotlib inline\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.metrics import r2_score"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Read dataset\n",
    "\n",
    "I'll read the dataset and get information about it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>Name</th>\n",
       "      <th>Location</th>\n",
       "      <th>Year</th>\n",
       "      <th>Kilometers_Driven</th>\n",
       "      <th>Fuel_Type</th>\n",
       "      <th>Transmission</th>\n",
       "      <th>Owner_Type</th>\n",
       "      <th>Mileage</th>\n",
       "      <th>Engine</th>\n",
       "      <th>Power</th>\n",
       "      <th>Seats</th>\n",
       "      <th>New_Price</th>\n",
       "      <th>Price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Maruti Wagon R LXI CNG</td>\n",
       "      <td>Mumbai</td>\n",
       "      <td>2010</td>\n",
       "      <td>72000</td>\n",
       "      <td>CNG</td>\n",
       "      <td>Manual</td>\n",
       "      <td>First</td>\n",
       "      <td>26.6 km/kg</td>\n",
       "      <td>998 CC</td>\n",
       "      <td>58.16 bhp</td>\n",
       "      <td>5.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Hyundai Creta 1.6 CRDi SX Option</td>\n",
       "      <td>Pune</td>\n",
       "      <td>2015</td>\n",
       "      <td>41000</td>\n",
       "      <td>Diesel</td>\n",
       "      <td>Manual</td>\n",
       "      <td>First</td>\n",
       "      <td>19.67 kmpl</td>\n",
       "      <td>1582 CC</td>\n",
       "      <td>126.2 bhp</td>\n",
       "      <td>5.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>12.50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Honda Jazz V</td>\n",
       "      <td>Chennai</td>\n",
       "      <td>2011</td>\n",
       "      <td>46000</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>Manual</td>\n",
       "      <td>First</td>\n",
       "      <td>18.2 kmpl</td>\n",
       "      <td>1199 CC</td>\n",
       "      <td>88.7 bhp</td>\n",
       "      <td>5.0</td>\n",
       "      <td>8.61 Lakh</td>\n",
       "      <td>4.50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Maruti Ertiga VDI</td>\n",
       "      <td>Chennai</td>\n",
       "      <td>2012</td>\n",
       "      <td>87000</td>\n",
       "      <td>Diesel</td>\n",
       "      <td>Manual</td>\n",
       "      <td>First</td>\n",
       "      <td>20.77 kmpl</td>\n",
       "      <td>1248 CC</td>\n",
       "      <td>88.76 bhp</td>\n",
       "      <td>7.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>6.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Audi A4 New 2.0 TDI Multitronic</td>\n",
       "      <td>Coimbatore</td>\n",
       "      <td>2013</td>\n",
       "      <td>40670</td>\n",
       "      <td>Diesel</td>\n",
       "      <td>Automatic</td>\n",
       "      <td>Second</td>\n",
       "      <td>15.2 kmpl</td>\n",
       "      <td>1968 CC</td>\n",
       "      <td>140.8 bhp</td>\n",
       "      <td>5.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>17.74</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Unnamed: 0                              Name    Location  Year  \\\n",
       "0           0            Maruti Wagon R LXI CNG      Mumbai  2010   \n",
       "1           1  Hyundai Creta 1.6 CRDi SX Option        Pune  2015   \n",
       "2           2                      Honda Jazz V     Chennai  2011   \n",
       "3           3                 Maruti Ertiga VDI     Chennai  2012   \n",
       "4           4   Audi A4 New 2.0 TDI Multitronic  Coimbatore  2013   \n",
       "\n",
       "   Kilometers_Driven Fuel_Type Transmission Owner_Type     Mileage   Engine  \\\n",
       "0              72000       CNG       Manual      First  26.6 km/kg   998 CC   \n",
       "1              41000    Diesel       Manual      First  19.67 kmpl  1582 CC   \n",
       "2              46000    Petrol       Manual      First   18.2 kmpl  1199 CC   \n",
       "3              87000    Diesel       Manual      First  20.77 kmpl  1248 CC   \n",
       "4              40670    Diesel    Automatic     Second   15.2 kmpl  1968 CC   \n",
       "\n",
       "       Power  Seats  New_Price  Price  \n",
       "0  58.16 bhp    5.0        NaN   1.75  \n",
       "1  126.2 bhp    5.0        NaN  12.50  \n",
       "2   88.7 bhp    5.0  8.61 Lakh   4.50  \n",
       "3  88.76 bhp    7.0        NaN   6.00  \n",
       "4  140.8 bhp    5.0        NaN  17.74  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataset = pd.read_csv(\"data/dataset.csv\")\n",
    "dataset.head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's first split the dataset into train and test datasets."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(dataset.iloc[:, :-1], \n",
    "                                                    dataset.iloc[:, -1], \n",
    "                                                    test_size = 0.3, \n",
    "                                                    random_state = 42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 4213 entries, 4201 to 860\n",
      "Data columns (total 13 columns):\n",
      "Unnamed: 0           4213 non-null int64\n",
      "Name                 4213 non-null object\n",
      "Location             4213 non-null object\n",
      "Year                 4213 non-null int64\n",
      "Kilometers_Driven    4213 non-null int64\n",
      "Fuel_Type            4213 non-null object\n",
      "Transmission         4213 non-null object\n",
      "Owner_Type           4213 non-null object\n",
      "Mileage              4212 non-null object\n",
      "Engine               4189 non-null object\n",
      "Power                4189 non-null object\n",
      "Seats                4185 non-null float64\n",
      "New_Price            580 non-null object\n",
      "dtypes: float64(1), int64(3), object(9)\n",
      "memory usage: 460.8+ KB\n"
     ]
    }
   ],
   "source": [
    "X_train.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exploratory Data Analysis\n",
    "\n",
    "Let's explore the various columns and draw information about how useful each column is. I'll also modify the test data based on training data."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Index\n",
    "\n",
    "The first column is the index for each data point and hence we can simply remove it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train = X_train.iloc[:, 1:]\n",
    "X_test = X_test.iloc[:, 1:]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Name\n",
    "\n",
    "Let's explore the various cars in the dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Mahindra XUV500 W8 2WD             35\n",
       "Maruti Swift VDI                   31\n",
       "Maruti Ritz VDi                    26\n",
       "Hyundai i10 Sportz                 25\n",
       "Maruti Swift Dzire VDI             24\n",
       "                                   ..\n",
       "BMW X5 xDrive 30d M Sport           1\n",
       "Mini Countryman Cooper D            1\n",
       "Mitsubishi Lancer 1.5 SFXi          1\n",
       "Hyundai i10 Magna Optional 1.1L     1\n",
       "Mercedes-Benz CLA 200 CDI Style     1\n",
       "Name: Name, Length: 1592, dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train[\"Name\"].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As it appears, there are several cars in the dataset, some of them with a count higher than 1.\n",
    "Sometimes the resale value of a car also depends on manufacturer of car and hence, I'll extract the manufacturer from this column and add it to the dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "make_train = X_train[\"Name\"].str.split(\" \", expand = True)\n",
    "make_test = X_test[\"Name\"].str.split(\" \", expand = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train[\"Manufacturer\"] = make_train[0]\n",
    "X_test[\"Manufacturer\"] = make_test[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's also confirm that there are no null values and identify all unique values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Count of cars')"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAtMAAAIyCAYAAAAJ7EYWAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8QZhcZAAAgAElEQVR4nOzdeZRV1Zn38e8DxaAiggyGQQRRw2wxRHBojNo4R2XQhKBRQWmTOAc1/bZJ1Awaog0ajVMkItoaZ4ghikFRY6IGFOcIqCjQGpCAqKgI7vePe6guELA41K2J72etWnXOPvvs89zLdfm7u/Y9N1JKSJIkSdp89aq7AEmSJKm2MkxLkiRJORmmJUmSpJwM05IkSVJOhmlJkiQpJ8O0JEmSlJNhWlKdFxGDI2JBRHwYEb2rux6AiJgREadUcw03R8TPqrOGqlYTXwuSajfDtKQKi4hvR8TMLIi8ExF/ioj9quC6KSJ224IhLgdOTyk1SSk9V1l1qVaqlNdCRMyPiH+vxLok1VKGaUkVEhHnAuOBXwA7AR2A3wBHV2ddFbQL8HIxLxARJcUcX5Wm6K+Fitjc14uvL6nmMkxL+lIRsQNwCfD9lNK9KaWPUkqfpZT+kFI6L+vTKCLGR8T/Zj/jI6JRduykiPjLemOWzTZnyw2uiYg/RsQHEfF0RHTOjj2enfJ8NiP+zQ3UVy8iLoyItyJicUTcEhE7ZDV9CNTPzn99I4+ve0Q8HBH/ioh/RsT/y9r3ioi/RcTybCb+6ohouN5j+H5EzAXmRsG4rIYVEfFiRPTYxFPbOSKeyfpOjogdy419V0S8GxHvR8TjEdG93LHDI+KV7LlaFBFjyh07MiJmZzX/NSJ6lTvWOyKezc77PdB4Y4Vt7DnNjnXMHvuJEfF2RLwXEf+1ibFujojfZH/J+DAinoyIr2SvkWUR8Y/ySy4i4ocR8XpW5ysRMbjcsZMi4i8RcXl27psRcVi54+vMGEfERRFx68ZeC5u6Vnb81Ih4tdzxPhExicKbyT9kj+f8iPh6RCxc79yyWrI67s5qWQGclD3Ha6+/NCLuXPsaKPccj4qIt4FHIqJxdv7S7N/37xGx08aed0lVwzAtqSL2phC87ttEn/8CBgClwJ7AXsCFm3GNbwEXA82BecDPAVJKA7Pje2Z/mv/9Bs49Kfs5ANgVaAJcnVL6NKXUpNz5ndc/MSK2B/4MPAi0BXYDpmeH1wDnAC0pPAcHAd9bb4hjgP5AN+BgYCCwB7ADcBywdBOP+TvASKANsBq4qtyxPwG7A62BZ4Hbyh27CfiPlNL2QA/gkeyx9AYmAP8BtACuB6ZkQbIhcD8wCdgRuAsYuonaTmIDz+l6ffYDvkrheflxRHTdxHjHUXg9tAQ+Bf6WPa6WwN3Af5fr+zrwbxSew4uBWyOiTbnj/YHXsnPHAjdFRGzi2mzitbDRa0XEscBFFP6dmgJHAUtTSicAbwPfyF6TYzd17XKOzh5rMwr/nmdQeP3sT+G1twy4Zr1z9ge6AocAJ2Z17kzh3/c04OMKXltSkRimJVVEC+C9lNLqTfQZAVySUlqcUlpCIZicsBnXuC+l9Ex2jdsohPKKGgH8d0rpjZTSh8B/At+Kiv1p/Ejg3ZTSFSmlT1JKH6SUngZIKc1KKT2VUlqdUppPIZzuv975l6aU/pVS+hj4DNge6AJESunVlNI7m7j2pJTSSymlj4AfAcdFRP3s2hOyWj6lEOj2XDsznF2nW0Q0TSktSyk9m7WPBq5PKT2dUlqTUppIIbgOyH4aAOOzvyrcDfx9E7VV5Dm9OKX0cUrpeeB5Cm+iNua+7Pn8hMKbsk9SSreklNYAvwfKZqZTSnellP43pfR59uZpLoU3Z2u9lVK6MTt3IoU3I7lmaL/kWqcAY1NKf08F81JKb+W5TuZvKaX7s2t9TCEM/1dKaWG5f+dh6z3HF2V/CVr7+moB7Jb9+85KKa3YgnokVQLDtKSKWAq0/JJw2hYoHzTeytoq6t1y2yspzIRW1IauXULFAtbOFGYnvyAi9oiIB7LlFisorBdvuV63BWs3UkqPUJi9vQZYHBE3RETTTVx7QbnttyiE3ZYRUT8iLsv+/L8CmJ/1WXvtocDhwFsR8VhE7J217wL8IFsCsDwilmePr232syillNa75sZU5DndnH+zf5bb/ngD+2XnRsR3yi1VWU5h9r3881523ZTSymxzc14vZb7kWht9beS0YL39XYD7yl37VQp/DdlpI+dMAh4C7ojCUqqxEdGgEuuTlINhWlJF/I3CDOcxm+jzvxTCwVodsjaAj4Bt1x6IiK9Ucn0buvZq1g1sG7OAwjKGDbkW+Aewe0qpKfD/gPWXE6R1dlK6KqXUl8Kyjz2A8zZx7Z3Xq/kz4D3g2xSWBPw7hT/rd8z6RHaNv6eUjqawBOR+4M5yj+XnKaVm5X62TSndDrwDtFtvOUSHTdS2Jc9pbhGxC3AjcDrQIqXUDHiJLz7vG7POaw3Y6GutAtdaAHxhaVAmrbe//mu8PtDqS85ZABy23r9X45TSog2dk/1F4eKUUjdgHwp/VfnOxh6fpKphmJb0pVJK7wM/Bq6JiGMiYtuIaBARh0XE2vWitwMXRkSriGiZ9b81O/Y80D0iSiOiMYU/Z2+Of7LxwLv22udERKeIaEJhBvn3X7IsZa0HgDYRcXa2tnj7iOifHdseWAF8GBFdgO9uaqCI+FpE9M9mCz8CPgE+38Qpx0dEt4jYlsIHPO/Oli5sT+HNy1IKAe0X5a7RMCJGRMQOKaXPsvrWXuNG4LSshoiI7SLiiGxd+N8ohOEzs3+7Iay7dGJ9W/KcbontKATIJQARcTKF2eKKmk1hOUqDiOgHDNuCa/0WGBMRfbPnc7csgMMXX5NzgMbZ892AwvrwRl9S63XAz9eOmf23s9G740TEARHRMwvqKyi8+drU60tSFTBMS6qQlNIVwLkUQsISCrNqp1OYGQX4GTATeAF4kcKHy36WnTuHQlj8M4U1qevc2aMCLgImZn8OP24DxydQ+BP448CbFELsGRV8XB8Ag4BvUFg+MJfCh+4AxlCYJf6AQlDd0Icfy2ua9VtGYVnEUuBXm+g/Cbg5u25j4Mys/Zbs/EXAK8BT6513AjA/WwJyGoX1zaSUZgKnUlhqsozCBzlPyo6tAoZk+/8Cvgncu4nacj+nWyKl9ApwBYXw/0+gJ/DkZgzxIwqzycsorNv/n7zXSindReGDsP9D4TVwP4UPbwJcSuHN4/KIGJO94fwehQC+iMKbqXXu7rEBVwJTgGkR8QGFf+f+m+j/FQofYFxBYUnIYxT+jSRVo1h3+ZwkSZKkinJmWpIkScrJMC1JkiTlZJiWJEmScjJMS5IkSTkZpiVJkqScKvJVuzVWy5YtU8eOHau7DEmSJNVxs2bNei+ltP6XMdXuMN2xY0dmzpxZ3WVIkiSpjouItzbU7jIPSZIkKSfDtCRJkpSTYVqSJEnKyTAtSZIk5WSYliRJknIyTEuSJEk5GaYlSZKknAzTkiRJUk6GaUmSJCknw/RWZNy4cXTv3p0ePXowfPhwPvnkk7JjZ555Jk2aNFmn/5133km3bt3o3r073/72t6u6XEmSpBrPML2VWLRoEVdddRUzZ87kpZdeYs2aNdxxxx0AzJw5k2XLlq3Tf+7cuVx66aU8+eSTvPzyy4wfP746ypYkSarRDNNbkdWrV/Pxxx+zevVqVq5cSdu2bVmzZg3nnXceY8eOXafvjTfeyPe//32aN28OQOvWraujZEmSpBrNML2VaNeuHWPGjKFDhw60adOGHXbYgYMPPpirr76ao446ijZt2qzTf86cOcyZM4d9992XAQMG8OCDD1ZT5ZIkSTVXSXUXoKqxbNkyJk+ezJtvvkmzZs049thjueWWW7jrrruYMWPGF/qvXr2auXPnMmPGDBYuXMjAgQN58cUXadasWdUXL0mSVEM5M72V+POf/0ynTp1o1aoVDRo0YMiQIfzkJz9h3rx57LbbbnTs2JGVK1ey2267AdC+fXuOOuooGjRoQKdOndhjjz2YO3duNT8KSZKkmsUwvZXo0KEDTz31FCtXriSlxPTp0zn33HN59913mT9/PvPnz2fbbbdl3rx5ABxzzDFlM9bvvfcec+bMYdddd63GRyBJklTzuMxjK9G/f3+GDRtGnz59KCkpoXfv3owePXqj/Q855BCmTZtGt27dqF+/Pr/61a9o0aJFFVYsSZJU80VKqbpryK1fv35p5syZ1V2GJEmS6riImJVS6rd+uzPTW4GXfnNUpY3V43tTKm0sSZKk2s4105IkSVJOhmlJkiQpJ8O0JEmSlJNhWpIkScrJMC1JkiTlZJiWJEmScjJMS5IkSTkZpiVJkqScDNOSJElSToZpSZIkKSfDtCRJkpSTYVqSJEnKyTAtSZIk5WSYliRJknIyTEuSJEk5GaYlSZKknAzTkiRJUk6GaUmSJCmnoobpiDgnIl6OiJci4vaIaBwRnSLi6YiYFxG/j4iGWd9G2f687HjHYtYmSZIkbamihemIaAecCfRLKfUA6gPfAn4JjEsp7QYsA0Zlp4wClmXt47J+kiRJUo1V7GUeJcA2EVECbAu8AxwI3J0dnwgck20fne2THT8oIqLI9UmSJEm5FS1Mp5QWAZcDb1MI0e8Ds4DlKaXVWbeFQLtsux2wIDt3dda/RbHq21yvvfYapaWlZT9NmzZl/PjxzJ49mwEDBlBaWkq/fv145plnALjtttvo1asXPXv2ZJ999uH555+v5kcgSZKkylZSrIEjojmF2eZOwHLgLuDQShh3NDAaoEOHDls6XIV99atfZfbs2QCsWbOGdu3aMXjwYE499VR+8pOfcNhhhzF16lTOP/98ZsyYQadOnXjsscdo3rw5f/rTnxg9ejRPP/10ldUrSZKk4ivmMo9/B95MKS1JKX0G3AvsCzTLln0AtAcWZduLgJ0BsuM7AEvXHzSldENKqV9KqV+rVq2KWP7GTZ8+nc6dO7PLLrsQEaxYsQKA999/n7Zt2wKwzz770Lx5cwAGDBjAwoULq6VWSZIkFU/RZqYpLO8YEBHbAh8DBwEzgUeBYcAdwInA5Kz/lGz/b9nxR1JKqYj15XbHHXcwfPhwAMaPH88hhxzCmDFj+Pzzz/nrX//6hf433XQThx12WFWXKUmSpCIr5prppyl8kPBZ4MXsWjcAFwDnRsQ8Cmuib8pOuQlokbWfC/ywWLVtiVWrVjFlyhSOPfZYAK699lrGjRvHggULGDduHKNGjVqn/6OPPspNN93EL3/pzUkkSZLqmqihk78V0q9fvzRz5swqvebkyZO55pprmDZtGgA77LADy5cvJyJIKbHDDjuULft44YUXGDx4MH/605/YY489qrTO8l76zVGVNlaP702ptLEkSZJqi4iYlVLqt36734C4mW6//fayJR4Abdu25bHHHgPgkUceYffddwfg7bffZsiQIUyaNKlag7QkSZKKp5hrpuucjz76iIcffpjrr7++rO3GG2/krLPOYvXq1TRu3JgbbrgBgEsuuYSlS5fyve99D4CSkhKqehZdkiRJxeUyj62AyzwkSZK2jMs8JEmSpErmMo8KWHzd+Eodr/VpZ1fqeJIkSaoezkxLkiRJORmmJUmSpJwM05IkSVJOhmlJkiQpJ8O0JEmSlJNhWpIkScrJMC1JkiTlZJiWJEmScjJMS5IkSTkZpiVJkqScDNOSJElSToZpSZIkKSfDtCRJkpSTYVqSJEnKyTAtSZIk5WSYliRJknIyTEuSJEk5GaYlSZKknAzTkiRJUk6GaUmSJCknw7QkSZKUk2FakiRJyskwLUmSJOVkmJYkSZJyMkxLkiRJORmmJUmSpJwM05IkSVJOhmlJkiQpJ8O0JEmSlJNhWpIkScrJMC1JkiTlZJiWJEmScjJMS5IkSTkZpiVJkqScDNOSJElSTkUL0xHx1YiYXe5nRUScHRE7RsTDETE3+9086x8RcVVEzIuIFyKiT7FqkyRJkipD0cJ0Sum1lFJpSqkU6AusBO4DfghMTyntDkzP9gEOA3bPfkYD1xarNkmSJKkyVNUyj4OA11NKbwFHAxOz9onAMdn20cAtqeApoFlEtKmi+iRJkqTNVlVh+lvA7dn2Timld7Ltd4Gdsu12wIJy5yzM2iRJkqQaqehhOiIaAkcBd61/LKWUgLSZ442OiJkRMXPJkiWVVKUkSZK0+apiZvow4NmU0j+z/X+uXb6R/V6ctS8Cdi53XvusbR0ppRtSSv1SSv1atWpVxLIlSZKkTauKMD2c/1viATAFODHbPhGYXK79O9ldPQYA75dbDiJJkiTVOCXFHDwitgMGAf9Rrvky4M6IGAW8BRyXtU8FDgfmUbjzx8nFrE2SJEnaUkUN0ymlj4AW67UtpXB3j/X7JuD7xaxHkiRJqkx+A6IkSZKUk2FakiRJyskwLUmSJOVkmJYkSZJyMkxLkiRJORmmJUmSpJwM05IkSVJOhmlJkiQpJ8O0JEmSlJNhWpIkScrJMC1JkiTlZJiWJEmScjJMS5IkSTkZpiVJkqScDNOSJElSToZpSZIkKSfDtCRJkpSTYVqSJEnKyTAtSZIk5WSYliRJknIyTEuSJEk5GaYlSZKknAzTkiRJUk6GaUmSJCknw7QkSZKUk2FakiRJyskwLUmSJOVkmJYkSZJyMkxLkiRJORmmJUmSpJwM05IkSVJOhmlJkiQpJ8O0JEmSlJNhWpIkScrJMC1JkiTlZJiWJEmScjJMS5IkSTkZpiVJkqScDNOSJElSToZpSZIkKaeihumIaBYRd0fEPyLi1YjYOyJ2jIiHI2Ju9rt51jci4qqImBcRL0REn2LWJkmSJG2pYs9MXwk8mFLqAuwJvAr8EJieUtodmJ7tAxwG7J79jAauLXJtkiRJ0hYpWpiOiB2AgcBNACmlVSml5cDRwMSs20TgmGz7aOCWVPAU0Cwi2hSrPkmSJGlLFXNmuhOwBPhdRDwXEb+NiO2AnVJK72R93gV2yrbbAQvKnb8wa5MkSZJqpGKG6RKgD3BtSqk38BH/t6QDgJRSAtLmDBoRoyNiZkTMXLJkSaUVK0mSJG2uYobphcDClNLT2f7dFML1P9cu38h+L86OLwJ2Lnd++6xtHSmlG1JK/VJK/Vq1alW04iVJkqQvU7QwnVJ6F1gQEV/Nmg4CXgGmACdmbScCk7PtKcB3srt6DADeL7ccRJIkSapxSoo8/hnAbRHREHgDOJlCgL8zIkYBbwHHZX2nAocD84CVWV9JkiSpxipqmE4pzQb6beDQQRvom4DvF7MeSZIkqTL5DYiSJElSToZpSZIkKSfDtCRJkpSTYVqSJEnKyTAtSZIk5WSYliRJknIyTEuSJEk5GaYlSZKknAzTkiRJUk6GaUmSJCknw7QkSZKUk2FakiRJyskwLUmSJOVkmJYkSZJyMkxLkiRJORmmJUmSpJwM05IkSVJOhmlJkiQpJ8O0JEmSlJNhWpIkScrJMC1JkiTlZJiWJEmScjJMS5IkSTkZpiVJkqScDNOSJElSToZpSZIkKSfDtCRJkpSTYVqSJEnKyTAtSZIk5WSYliRJknIyTEuSJEk5GaYlSZKknAzTkiRJUk6GaUmSJCknw7QkSZKUk2FakiRJyskwLUmSJOVkmJYkSZJyMkxLkiRJORmmJUmSpJy+NExHxFkR0TQKboqIZyPi4IoMHhHzI+LFiJgdETOzth0j4uGImJv9bp61R0RcFRHzIuKFiOizZQ9NkiRJKq6KzEyPTCmtAA4GmgMnAJdtxjUOSCmVppT6Zfs/BKanlHYHpmf7AIcBu2c/o4FrN+MakiRJUpWrSJiO7PfhwKSU0svl2vI4GpiYbU8EjinXfksqeApoFhFttuA6kiRJUlFVJEzPiohpFML0QxGxPfB5BcdPwLSImBURo7O2nVJK72Tb7wI7ZdvtgAXlzl2YtUmSJEk1UsmmDkZEAD8GWgFvpJRWRkQL4OQKjr9fSmlRRLQGHo6If5Q/mFJKEZE2p+AslI8G6NChw+acKkmSJFWqTc5Mp5QSMDWl9GxKaXnWtjSl9EJFBk8pLcp+LwbuA/YC/rl2+Ub2e3HWfRGwc7nT22dt6495Q0qpX0qpX6tWrSpShiRJklQUFVnm8WxEfG1zB46I7bIlIUTEdhQ+wPgSMAU4Met2IjA5254CfCe7q8cA4P1yy0EkSZKkGmeTyzwy/YEREfEW8BGFDx+mlFKvLzlvJ+C+wkoRSoD/SSk9GBF/B+6MiFHAW8BxWf+pFNZlzwNWUvGlJJIkSVK1qEiYPiTPwCmlN4A9N9C+FDhoA+0J+H6ea0mSJEnV4UvDdErpLYDsQ4SNi16RJEmSVEtU5BsQj4qIucCbwGPAfOBPRa5LkiRJqvEq8gHEnwIDgDkppU4Ulmg8VdSqJEmSpFqgImH6s2ydc72IqJdSehTo92UnSZIkSXVdRT6AuDwimgCPA7dFxGIKd/WQJEmStmoVmZk+msKt6s4BHgReB75RzKIkSZKk2qAiM9OtgXdSSp8AEyNiGwr3kF5a1MokSZKkGq4iM9N3AZ+X21+TtUmSJElbtYqE6ZKU0qq1O9l2w+KVJEmSJNUOFQnTSyLiqLU7EXE08F7xSpIkSZJqh4qsmT6Nwl08rs72FwInFK8kSZIkqXaoyNeJvw4MyG6PR0rpw6JXJUmSJNUCFZmZBgzRkiRJ0voqsmZakiRJ0gZsNExHxLHZ705VV44kSZJUe2xqZvo/s9/3VEUhkiRJUm2zqTXTSyNiGtApIqasfzCldNQGzpEkSZK2GpsK00cAfYBJwBVVU44kSZJUe2w0TGffdPhUROyTUlrirfEkSZKkdVXkbh47RcRzwMvAKxExKyJ6FLkuSZIkqcarSJi+ATg3pbRLSqkD8IOsTZIkSdqqVSRMb5dSenTtTkppBrBd0SqSJEmSaomKfAPiGxHxIwofRAQ4HnijeCVJkiRJtUNFZqZHAq2Aeyncc7pl1iZJkiRt1b40TKeUlqWUzkwp9Ukp9U0pnZ1SWlYVxUlVac2aNfTu3ZsjjzwSgBEjRvDVr36VHj16MHLkSD777DMA/vGPf7D33nvTqFEjLr/88uosWZIkVbOKzExLW4Urr7ySrl27lu2PGDGCf/zjH7z44ot8/PHH/Pa3vwVgxx135KqrrmLMmDHVVaokSaohDNMSsHDhQv74xz9yyimnlLUdfvjhRAQRwV577cXChQsBaN26NV/72tdo0KBBdZUrSZJqiC8N0xGxb0XapNrs7LPPZuzYsdSr98X/JD777DMmTZrEoYceWg2VSZKkmqwiM9O/rmCbVCs98MADtG7dmr59+27w+Pe+9z0GDhzIv/3bv1VxZZIkqabb6K3xImJvYB+gVUScW+5QU6B+sQuTqsqTTz7JlClTmDp1Kp988gkrVqzg+OOP59Zbb+Xiiy9myZIlXH/99dVdpiRJqoE2NTPdEGhCIXBvX+5nBTCs+KVJVePSSy9l4cKFzJ8/nzvuuIMDDzyQW2+9ld/+9rc89NBD3H777Rtc/iFJkrTRmemU0mPAYxFxc0rprSqsSaoRTjvtNHbZZRf23ntvAIYMGcKPf/xj3n33Xfr168eKFSuoV68e48eP55VXXqFp06bVXLEkSapqFfkGxEYRcQPQsXz/lNKBxSpKqi5f//rX+frXvw7A6tWrN9jnK1/5StmdPSRJ0tatImH6LuA64LfAmuKWI1W9228+pNLGGn7SQ5U2liRJqvkqEqZXp5SuLXolkiRJUi1TkU9V/SEivhcRbSJix7U/Ra9MkiRJquEqMjN9Yvb7vHJtCdi18suRJEmSao8vDdMppU5VUYgkSZJU23xpmI6I72yoPaV0S+WXI0mSJNUeFVnm8bVy242Bg4BnAcO0JEmStmoVWeZxRvn9iGgG3FHRC0REfWAmsCildGREdMrObwHMAk5IKa2KiEYUAnpfYCnwzZTS/IpeR5IkSapqeb4j+SNgc9ZRnwW8Wm7/l8C4lNJuwDJgVNY+CliWtY/L+kmSJEk11peG6Yj4Q0RMyX7+CLwG3FeRwSOiPXAEhS98ISICOBC4O+syETgm2z462yc7flDWX5IkSaqRKrJm+vJy26uBt1JKFf0u5fHA+cD22X4LYHlKae33NC8E2mXb7YAFACml1RHxftb/vQpeS5IkSapSXzoznVJ6DPgHhUDcHFhVkYEj4khgcUpp1hZV+MVxR0fEzIiYuWTJksocWpIkSdosFVnmcRzwDHAscBzwdEQMq8DY+wJHRcR8Ch84PBC4EmgWEWtnxNsDi7LtRcDO2TVLgB0ofBBxHSmlG1JK/VJK/Vq1alWBMiRJkqTiqMgHEP8L+FpK6cSU0neAvYAffdlJKaX/TCm1Tyl1BL4FPJJSGgE8CqwN4ycCk7PtKfzfty0Oy/qnCj8SSZIkqYpVJEzXSyktLre/tILnbcwFwLkRMY/CmuibsvabgBZZ+7nAD7fgGpIkSVLRVeQDiA9GxEPA7dn+N4E/bc5FUkozgBnZ9hsUZrfX7/MJhaUkkiRJUq1QkS9tOS8ihgD7ZU03pJQqdGs8SZIkqS7baJiOiN2AnVJKT6aU7gXuzdr3i4jOKaXXq6pISZIkqSba1Nrn8cCKDbS/nx2TJEmStmqbCtM7pZReXL8xa+tYtIokSZKkWmJTYbrZJo5tU9mFSJIkSbXNpsL0zIg4df3GiDgFqNRvNZQkSZJqo03dzeNs4L6IGMH/hed+QENgcLELkyRJkmq6jYbplNI/gX0i4gCgR9b8x5TSI1VSmSRJklTDVeQ+049S+ApwSZIkSeVsydeCS5IkSVs1w7QkSZKUk2FakiRJyskwLUmSJOVkmJYkSZJyMkxLkiRJORmmJUmSpJwM05IkSVJOhmlJkiQpJ8O0JEmSlJNhWpIkScrJMC1JkiTlZJiWJEmScjJMS5IkSTkZpiVJkqScDNOSJElSToZpSZIkKSfDtCRJkpSTYVqSJEnKyTAtSZIk5WSYliRJknIyTEuSJEk5GaYlSZKknAzTkiRJUk6GaUmSJCknw7QkSZKUk2FakiRJyskwLUmSJOVkmJbqgAULFnDAAQfQrVs3unfvzpVXXgnA888/z0RjFBcAACAASURBVN57703Pnj35xje+wYoVKwCYP38+22yzDaWlpZSWlnLaaadVZ/mSJNVaJdVdgKQtV1JSwhVXXEGfPn344IMP6Nu3L4MGDeKUU07h8ssvZ//992fChAn86le/4qc//SkAnTt3Zvbs2dVcuSRJtZsz01Id0KZNG/r06QPA9ttvT9euXVm0aBFz5sxh4MCBAAwaNIh77rmnOsuUJKnOKVqYjojGEfFMRDwfES9HxMVZe6eIeDoi5kXE7yOiYdbeKNuflx3vWKzapLps/vz5PPfcc/Tv35/u3bszefJkAO666y4WLFhQ1u/NN9+kd+/e7L///jzxxBPVVa4kSbVaMWemPwUOTCntCZQCh0bEAOCXwLiU0m7AMmBU1n8UsCxrH5f1k7QZPvzwQ4YOHcr48eNp2rQpEyZM4De/+Q19+/blgw8+oGHDhkBhJvvtt9/mueee47//+7/59re/XbaeWpIkVVzRwnQq+DDbbZD9JOBA4O6sfSJwTLZ9dLZPdvygiIhi1SfVNZ999hlDhw5lxIgRDBkyBIAuXbowbdo0Zs2axfDhw+ncuTMAjRo1okWLFgD07duXzp07M2fOnGqrXZKk2qqoa6Yjon5EzAYWAw8DrwPLU0qrsy4LgXbZdjtgAUB2/H2gRTHrk+qKlBKjRo2ia9eunHvuuWXtixcvBuDzzz/nZz/7WdldO5YsWcKaNWsAeOONN5g7dy677rpr1RcuSVItV9S7eaSU1gClEdEMuA/osqVjRsRoYDRAhw4dtnQ4qU548sknmTRpEj179qS0tBSAX/ziF8ydO5drrrkGgCFDhnDyyScD8Pjjj/PjH/+YBg0aUK9ePa677jp23HHHaqtfkqTaqkpujZdSWh4RjwJ7A80ioiSbfW4PLMq6LQJ2BhZGRAmwA7B0A2PdANwA0K9fv1QV9Us13X777UdKG/7P4ayzzvpC29ChQxk6dGixy5Ikqc4rWpiOiFbAZ1mQ3gYYROFDhY8Cw4A7gBOBydkpU7L9v2XHH0kbSweSyvzyjkMqbawLvvVQpY0lSdLWoJgz022AiRFRn8La7DtTSg9ExCvAHRHxM+A54Kas/03ApIiYB/wL+FYRa5MkSZK2WNHCdErpBaD3BtrfAPbaQPsnwLHFqkeSJEmqbH4DoiRJkpSTYVqSJEnKyTAtSZIk5WSYliRJknIyTEuSJEk5GaYlSZKknAzTkiRJUk6GaUmSJCknw7QkSZKUk2FakiRJyskwLUmSJOVkmJYkSZJyMkxLkiRJORmmJUmSpJwM05IkSVJOhmlJkiQpJ8O0JEmSlJNhWpIkScrJMC1JkiTlZJiWJEmScjJMS5IkSTkZpiVJkqScDNOSJElSTnUmTC9YsIADDjiAbt260b17d6688koAzjvvPLp06UKvXr0YPHgwy5cvB+Dhhx+mb9++9OzZk759+/LII49UZ/mSJEmqhepMmC4pKeGKK67glVde4amnnuKaa67hlVdeYdCgQbz00ku88MIL7LHHHlx66aUAtGzZkj/84Q+8+OKLTJw4kRNOOKGaH4FUM23uG9WlS5dywAEH0KRJE04//fTqLF2SpKKrM2G6TZs29OnTB4Dtt9+erl27smjRIg4++GBKSkoAGDBgAAsXLgSgd+/etG3bFoDu3bvz8ccf8+mnn1ZP8arzNhZI77rrLrp37069evWYOXNmWf9Vq1Zx8skn07NnT/bcc09mzJhRTZVv/hvVxo0b89Of/pTLL7+82mqWJKmq1JkwXd78+fN57rnn6N+//zrtEyZM4LDDDvtC/3vuuYc+ffrQqFGjqipRW5mNBdIePXpw7733MnDgwHX633jjjQC8+OKLPPzww/zgBz/g888/r47SN/uN6nbbbcd+++1H48aNq6VeSZKqUkl1F1DZPvzwQ4YOHcr48eNp2rRpWfvPf/5zSkpKGDFixDr9X375ZS644AKmTZtW1aVqK9KmTRvatGkDrBtIBw0atMH+r7zyCgceeCAArVu3plmzZsycOZO99tqrymrekE29Uf3mN79ZTVVJklR96tTM9GeffcbQoUMZMWIEQ4YMKWu/+eabeeCBB7jtttuIiLL2hQsXMnjwYG655RY6d+5cHSVrK7SxQFrennvuyZQpU1i9ejVvvvkms2bNYsGCBVVY5Rdt7htVSZK2BnVmZjqlxKhRo+jatSvnnntuWfuDDz7I2LFjeeyxx9h2223L2pcvX84RRxzBZZddxr777lsdJWsrtLFAur6RI0fy6quv0q9fP3bZZRf22Wcf6tevX4WVruvL3qhOnz59nTeqkiRtLepMmH7yySeZNGkSPXv2pLS0FIBf/OIXnHnmmXz66adlf04fMGAA1113HVdffTXz5s3jkksu4ZJLLgFg2rRptG7dutoeg+q2jQXSDSkpKWHcuHFl+/vssw977LFHsUvcoM19oypJ0takzoTp/fbbj5TSF9oPP/zwDfa/8MILufDCC4tdlgRsPJBuzMqVK0kpsd122/Hwww9TUlJCt27dqqDSL9rcN6oAHTt2ZMWKFaxatYr777+fadOmVVv9kiQVU50J01JNtrFA+umnn3LGGWewZMkSjjjiCEpLS3nooYdYvHgxhxxyCPXq1aNdu3ZMmjSp2mrf3DeqUFgXLknS1qBOhOkl195aqeO1+u7xlTqetLFACjB48OAvtHXs2JHXXnut2GVVyFn3HFppY1059MFKG0uSpJqgToRpqSa7ftIhlTbWf5zwUKWNJUmStlydujWeJEmSVJUM05IkSVJOhmlJkiQpJ8N0DTFy5Ehat25Njx49ytqef/559t57b3r27Mk3vvENVqxYAcDDDz9M37596dmzJ3379uWRRx6prrIlSZK2aobpGuKkk07iwQfXvdPBKaecwmWXXcaLL77I4MGD+dWvfgVAy5Yt+cMf/sCLL77IxIkTOeGEE6qjZEmSpK1e0cJ0ROwcEY9GxCsR8XJEnJW17xgRD0fE3Ox386w9IuKqiJgXES9ERJ9i1VYTDRw4kB133HGdtjlz5jBw4EAABg0axD333ANA7969adu2LQDdu3fn448/5tNPP63agiVJklTUmenVwA9SSt2AAcD3I6Ib8ENgekppd2B6tg9wGLB79jMauLaItdUK3bt3Z/LkyQDcddddLFiw4At97rnnHvr06UOjRo2qujxJkqStXtHCdErpnZTSs9n2B8CrQDvgaGBi1m0icEy2fTRwSyp4CmgWEW2KVV9tMGHCBH7zm9/Qt29fPvjgAxo2bLjO8ZdffpkLLriA66+/vpoqlGqHDX0mYfbs2QwYMIDS0lL69evHM888A8DkyZPp1atXWftf/vKX6ipbklQLVMma6YjoCPQGngZ2Sim9kx16F9gp224HlJ96XZi1bbW6dOnCtGnTmDVrFsOHD6dz585lxxYuXMjgwYO55ZZb1mmX9EUb+kzC+eefz09+8hNmz57NJZdcwvnnnw/AQQcdxPPPP8/s2bOZMGECp5xySnWULEmqJYoepiOiCXAPcHZKaUX5Y6nw/cob/o7ljY83OiJmRsTMJUuWVGKlNc/ixYsB+Pzzz/nZz37GaaedBsDy5cs54ogjuOyyy9h3332rs0SpVtjQZxIiouwOOe+//37Z5xCaNGlCRADw0UcflW1LkrQhRQ3TEdGAQpC+LaV0b9b8z7XLN7Lfi7P2RcDO5U5vn7WtI6V0Q0qpX0qpX6tWrYpXfBUbPnw4e++9N6+99hrt27fnpptu4vbbb2ePPfagS5cutG3blpNPPhmAq6++mnnz5nHJJZdQWlpKaWlpWfCWVDHjx4/nvPPOY+edd2bMmDFceumlZcfuu+8+unTpwhFHHMGECROqsUpJUk1XUqyBozCdcxPwakrpv8sdmgKcCFyW/Z5crv30iLgD6A+8X245SJ13++23b7D9rLPO+kLbhRdeyIUXXljskqQ67dprr2XcuHEMHTqUO++8k1GjRvHnP/8ZgMGDBzN48GAef/xxfvSjH5W1S5K0vqKFaWBf4ATgxYiYnbX9Pwoh+s6IGAW8BRyXHZsKHA7MA1YCJxexthpl0TXfr7Sx2n3/mkobS6rLJk6cyJVXXgnAscceu8G10QMHDuSNN97gvffeo2XLllVdoiSpFihamE4p/QXY2GLDgzbQPwGVlyolaRPatm3LY489xte//nUeeeQRdt99dwDmzZtH586diQieffZZPv30U1q0aFHN1UqSaqpizkxLUo0wfPhwZsyYwXvvvUf79u25+OKLufHGGznrrLNYvXo1jRs35oYbbgAK926/5ZZbaNCgAdtssw2///3v/RCiJGmjDNOS6ryNfSZh1qxZX2i74IILuOCCC4pdkiSpjqiS+0yr7tvQl2IA/PrXv6ZLly5079697D6+8+fPZ5tttim7E8naW/5JkiTVNs5Mq1KcdNJJnH766XznO98pa3v00UeZPHkyzz//PI0aNVrn9n2dO3dm9uzZGxpKqlSH33dRpY01dXDljSVJqhucmVal2NCXYlx77bX88Ic/pFGjRgC0bt26OkqTJEkqGsO0imbOnDk88cQT9O/fn/3335+///3vZcfefPNNevfuzf77788TTzxRjVVKkiTl5zIPFc3q1av517/+xVNPPcXf//53jjvuON544w3atGnD22+/TYsWLZg1axbHHHMML7/8Mk2bNq3ukiVJkjaLM9Mqmvbt2zNkyBAigr322ot69erx3nvv0ahRo7L79vbt25fOnTszZ86caq5WkiRp8xmmVTTHHHMMjz76KFBY8rFq1SpatmzJkiVLWLNmDQBvvPEGc+fOZdddd63OUiVJknJxmYcqxYa+FGPkyJGMHDmSHj160LBhQyZOnEhE8Pjjj/PjH/+YBg0aUK9ePa677rovfHhRkiSpNjBMq1Js7Esxbr311i+0DR06lKFDhxa7JEmSpKJzmYckSZKUkzPT2mJP3HhkpY31b6c+UGljSZIkFZsz05IkSVJOhmlJkiQpJ8O0JEmSlJNhWpIkScrJMC1JkiTlZJiWJEmScjJMS5IkSTkZpiVJkqScDNOSqt3IkSNp3bo1PXr0KGs777zz6NKlC7169WLw4MEsX7687NgLL7zA3nvvTffu3enZsyeffPJJdZQtSZJhWrXD5oYtgLfffpsmTZpw+eWXV3W52kwnnXQSDz744DptgwYN4qWXXuKFF15gjz324NJLLwVg9erVHH/88Vx33XW8/PLLzJgxgwYNGlRH2ZIkGaZVO2xO2Frr3HPP5bDDDqvKMpXTwIED2XHHHddpO/jggykpKQFgwIABLFy4EIBp06bRq1cv9txzTwBatGhB/fr1q7ZgSZIyhmnVCpsTtgDuv/9+OnXqRPfu3au0ThXHhAkTyt4YzZkzh4jgkEMOoU+fPowdO7aaq5Mkbc0M06oTyoetDz/8kF/+8pf85Cc/qeaqVBl+/vOfU1JSwogRI4DCMo+//OUv3HbbbfzlL3/hvvvuY/r06dVcpSRpa2WYVq23fti66KKLOOecc2jSpEk1V6YtdfPNN/PAAw9w2223EREAtG/fnoEDB9KyZUu23XZbDj/8cJ599tlqrlSStLUqqe4CpC2xNmxNnz69LGw9/fTT3H333Zx//vksX76cevXq0bhxY04//fRqrlab48EHH2Ts2LE89thjbLvttmXthxxyCGPHjmXlypU0bNiQxx57jHPOOacaK5Ukbc0M06q1Nha2nnjiibLtiy66iCZNmhika7jhw4czY8YM3nvvPdq3b8/FF1/MpZdeyqeffsqgQYOAwrr46667jubNm3Puuefyta99jYjg8MMP54gjjqjmRyBJ2loZplUrbE7YUu1z++23f6Ft1KhRG+1//PHHc/zxxxezJEmSKsQwrVphc8PWWhdddFERqpEkSSowTEuqVodNPrHSxvrT0RMrbSxJkirCMK0a748TKu+LV44Y+adKG0uSJMlb40mSJEk5GaYlSZKknAzTkiRJUk6GaUmSJCknw7Qk1SJXXnklPXr0oHv37owfPx4o3AKyXbt2lJaWUlpaytSpU6u5Sknaeng3D0mqJV566SVuvPFGnnnmGRo2bMihhx7KkUceCcA555zDmDFjqrlCSdr6GKYlqZZ49dVX6d+/P9tuuy0A+++/P/fee281VyVJW7eiLfOIiAkRsTgiXirXtmNEPBwRc7PfzbP2iIirImJeRLwQEX2KVZck1VY9evTgiSeeYOnSpaxcuZKpU6eyYMECAK6++mp69erFyJEjWbZsWTVXKklbj2Kumb4ZOHS9th8C01NKuwPTs32Aw4Dds5/RwLVFrEuSaqWuXbtywQUXcPDBB3PooYdSWlpK/fr1+e53v8vrr7/O7NmzadOmDT/4wQ+qu1RJ2moULUynlB4H/rVe89HA2u/7nQgcU679llTwFNAsItoUqzZJKpZx48bRvXt3evTowfDhw/nkk08YNWoUe+65J7169WLYsGF8+OGHuccfNWoUs2bN4vHHH6d58+bsscce7LTTTtSvX5969epx6qmn8swzz1TiI5IkbUpV381jp5TSO9n2u8BO2XY7YEG5fguzti+IiNERMTMiZi5ZsqR4lUrSZlq0aBFXXXUVM2fO5KWXXmLNmjXccccdjBs3jueff54XXniBDh06cPXVV+e+xuLFiwF4++23uffee/n2t7/NO++8U3b8vvvuo0ePHlv8WCRJFVNtH0BMKaWISDnOuwG4AaBfv36bfb4kFdPq1av5+OOPadCgAStXrqRt27Y0bdoUgJQSH3/8MRGRe/yhQ4eydOlSGjRowDXXXEOzZs0444wzmD17NhFBx44duf766yvr4UiSvkRVh+l/RkSblNI72TKOxVn7ImDncv3aZ22SVGu0a9eOMWPG0KFDB7bZZhsOPvhgDj74YABOPvlkpk6dSrdu3bjiiityX+OJJ574QtukSZNyjydJ2jJVHaanACcCl2W/J5drPz0i7gD6A++XWw4iSbXCsmXLmDx5Mm+++SbNmjXj2GOP5dZbb+X444/nd7/7HWvWrOGMM87g97//PSeffPKXjnfEPb+ttNr+OPSUShtLkvR/inlrvNuBvwFfjYiFETGKQogeFBFzgX/P9gGmAm8A84Abge8Vqy5JKpY///nPdOrUiVatWtGgQQOGDBnCX//617Lj9evX51vf+hb33HNPNVYpSapMRZuZTikN38ihgzbQNwHfL1YtklQVOnTowFNPPcXKlSvZZpttmD59Ov369WPevHnstttupJSYMmUKXbp0qe5SJUmVxG9AlKRK0r9/f4YNG0afPn0oKSmhd+/ejB49mgMPPJAVK1aQUmLPPffk2mu9lb4k1RWGaUmqRBdffDEXX3zxOm1PPvlkNVUjSSq2qr7PtCRJRbN8+XKGDRtGly5d6Nq1K3/729+46KKLaNeuHaWlpZSWljJ16tTqLlNSHeLMtCTldMS94yt1vD8OObtSx9sanXXWWRx66KHcfffdrFq1ipUrV/LQQw9xzjnnMGbMmOouT1IdZJiWJNUJ77//Po8//jg333wzAA0bNqRhw4bVW5SkOs9lHpKkOuHNN9+kVatWnHzyyfTu3ZtTTjmFjz76CICrr76aXr16MXLkSJYtW1bNlUqqSwzTkqQ6YfXq1Tz77LN897vf5bnnnmO77bbjsssu47vf/S6vv/46s2fPpk2bNvzgBz+o7lIl1SGGaUlSndC+fXvat29P//79ARg2bBjPPvssO+20E/Xr16devXqceuqpPPPMM9VcqaS6xDAtSaoTvvKVr7Dzzjvz2muvATB9+nS6devGO++8U9bnvvvuo0ePHtVVoqQ6yA8gSpLqjF//+teMGDGCVatWseuuu/K73/2OM888k9mzZxMRdOzYkeuvv766y5RUhximJUl1RmlpKTNnzlynbdKkSdVUjaStgcs8JEmSpJycmZYk1UpH3/1QpY01edghlTaWpK2LM9OSJElSToZpSZK2ImvWrKF3794ceeSRQOHLbvr3789uu+3GN7/5TVatWlXNFUq1i2FakqStyJVXXknXrl3L9i+44ALOOecc5s2bR/PmzbnpppuqsTqp9jFMS5K0lVi4cCF//OMfOeWUUwBIKfHII48wbNgwAE488UTuv//+6ixRqnUM05IkbSXOPvtsxo4dS716hf/9///23jxMrqra338/IUAQCIMCBoLMkECAEMI8SMSIzEOAGMMVSNDL74oEERkuepn8gUwKIiKgQJgCgaAgMs8xDIFAQgAB75UoIDIps0IC6/vH2pWubqo7SZ19qror632efrrrVNfau6tPnbP22mt91ptvvsmyyy5L796uR9C/f39efvnlZk4xCHoc4UwHQRAEwULAzTffzIorrsimm27a7KkEQUsR0nhBEARBsBAwZcoUbrrpJm655Rb+/e9/88477zBu3Djeeust5syZQ+/evXnppZdYZZVVmj3VIOhRRGQ6CIIgAODFF19k2LBhrL/++mywwQace+65AMyYMYOtttqKDTfckN1335133nmnyTMN6uG0007jpZdeYtasWVxzzTV86Utf4qqrrmLYsGFcf/31AIwfP54999yzyTMNgp5FONNBEAQBAL179+bss8/mmWee4eGHH+b888/nmWee4ZBDDuHHP/4xM2fOZO+99+bMM89s9lSDjJx++un85Cc/Ye211+bNN99k7NixzZ5SEPQoIs0jCIIgAKBfv37069cPgKWXXpqBAwfy8ssv8/zzz7P99tsDMHz4cHbaaSdOOeWUZk41KMgOO+zADjvsAMCaa67J1KlTmzuhIOjBRGQ6CIIg+BSzZs3iiSeeYIsttmCDDTbgxhtvBOC6667jxRdfbPLsgiAIug8RmQ6CIAja8d577zFixAjOOecc+vbtyyWXXMLhhx/OKaecwh577MFiiy3W7CkG88EJv/lbNlsn7b1yNltB0GpEZDoIgiCYy+zZsxkxYgSjR49mn332AWDAgAHccccdTJs2jVGjRrHWWms1eZbBwsiYMWNYccUVGTRo0Nxj06dPZ8stt2Tw4MEMHTq0W6er1Jp/FPe2BuFMB0EQBIB3wxs7diwDBw7kyCOPnHv8tddeA+CTTz7hRz/6EYceemizptjS1HK2Ro4cyeDBgxk8eDCrr746gwcPbuIMm8tBBx3Ebbfd1u7Y0UcfzQknnMD06dM5+eSTOfroo5s0u3lTa/45i3trnT8A5513HgMGDGCDDTbo1u9PTyac6SAIggBwHeIrrriCe+65Z64Dd8sttzBhwgTWXXddBgwYwMorr8zBBx/c7Km2JLWcrWuvvZbp06czffp0RowYMXe3YGFk++23Z/nll293TNLcaO7bb7/Nyit333SUWvPvWNw7adKkuu3XOn/uvfdebrzxRmbMmMHTTz/NUUcdVbf9oHMiZzoIgiAAYNttt8XMaj43bty4Bs9m4WP77bdn1qxZNZ8zMyZOnMg999zT2El1c8455xx22mknjjrqKD755BMefPDBZk9pgagU9+61116Fi3trnT8XXHABxx57LIsvvjgAK664YpHpBp0QznQQBMFCym7XX5XN1s37jp7n74wZM2ZuS+unnnoKcHWQE088kT/+8Y9MnTqVoUOHZptTbpo5/8mTJ7PSSiuxzjrrlGK/p3LBBRfw05/+lBEjRjBx4kTGjh3LXXfd1expzTdlF/c+//zzTJ48meOPP54+ffpw1llnsdlmm2UdI4g0jyAIgqBB1NqGHjRoEDfccMPcre7uTDPnP2HCBEaNGlXqGD2R8ePHz0192W+//bp1AWItyi7unTNnDv/4xz94+OGHOfPMM9l///073X0K6iec6SAIgqAh1MoZHThwIOutt16TZrRgNGv+c+bM4YYbbmDkyJGljtMTWXnllbn//vsBuOeee3pc5L7s4t7+/fuzzz77IInNN9+cXr168cYbbxS2+9xzz82tqxg8eDB9+/blnHPOyTDjnkmkeQRBEARBN+auu+5iwIAB9O/fv9lTaSqjRo3ivvvu44033qB///6cdNJJXHzxxYwbN445c+bQp08fLrroomZPs1Nqzf+9997j/PPPB2CfffbJXty71157ce+99zJs2DCef/55PvroIz73uc8Vtrveeusxffp0AD7++GNWWWUV9t5778J2eyrhTAdBEARBN6CWszV27FiuueaaHpfi8eKLL/KNb3yDV199FUl861vfKlzEOmHChJrHp02bVshuo+hs/rmKe2udP2PGjGHMmDEMGjSIxRZbjPHjxyMpy3gV7r77btZaay1WW221LPbKOHfKJpzpIAiCIOgGdOZsXXbZZY2dSAZ69+7N2WefzZAhQ3j33XfZdNNNGT58OOuvv36zpzZf1Co2XRCeP//VrPNZ99srzfN3Ojt/rrzyyqxz6UjuxV4jzp2i/9+OhDMdBEEQBE1g/0nPZrM1ccSAbLZy0K9fP/r16wfA0ksvzcCBA3n55ZcXyCG69driub0Vdh65YKkNBx10EIcddhjf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\n",
      "text/plain": [
       "<Figure size 864x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize = (12, 8))\n",
    "plot = sns.countplot(x = 'Manufacturer', data = X_train)\n",
    "plt.xticks(rotation = 90)\n",
    "for p in plot.patches:\n",
    "    plot.annotate(p.get_height(), \n",
    "                        (p.get_x() + p.get_width() / 2.0, \n",
    "                         p.get_height()), \n",
    "                        ha = 'center', \n",
    "                        va = 'center', \n",
    "                        xytext = (0, 5),\n",
    "                        textcoords = 'offset points')\n",
    "\n",
    "plt.title(\"Count of cars based on manufacturers\")\n",
    "plt.xlabel(\"Manufacturer\")\n",
    "plt.ylabel(\"Count of cars\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Maximum cars in the dataset are by the manufacturer **Maruti** and there are no null values.\n",
    "\n",
    "I'll also drop the `Name` column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train.drop(\"Name\", axis = 1, inplace = True)\n",
    "X_test.drop(\"Name\", axis = 1, inplace = True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Location\n",
    "\n",
    "Location should not be a determinant for the price of a car and I'll safely remove it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train.drop(\"Location\", axis = 1, inplace = True)\n",
    "X_test.drop(\"Location\", axis = 1, inplace = True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Year\n",
    "\n",
    "Year has no significance on its own unless we try to extract how old a car is from this and see how its resale price may get affected."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "curr_time = datetime.datetime.now()\n",
    "X_train['Year'] = X_train['Year'].apply(lambda x : curr_time.year - x)\n",
    "X_test['Year'] = X_test['Year'].apply(lambda x : curr_time.year - x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Fuel_Type, Transmission,  and Owner_Type\n",
    "\n",
    "All these columns are categorical columns which should be converted to dummy variables before being used."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Kilometers_Driven\n",
    "\n",
    "`Kilometers_Driven` is a numerical column with a certain range of values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4201     77000\n",
       "4383     19947\n",
       "1779     70963\n",
       "4020    115195\n",
       "3248     58752\n",
       "         ...  \n",
       "3772     27000\n",
       "5191      9000\n",
       "5226    140000\n",
       "5390     76414\n",
       "860      98000\n",
       "Name: Kilometers_Driven, Length: 4213, dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train[\"Kilometers_Driven\"]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The data range is really varied and the high values might affect prediction, thus, it is really important that scaling be applied to this column for sure."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Mileage\n",
    "\n",
    "This column defines the mileage of the car. We need to extract the numerical value out of each string and save it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "mileage_train = X_train[\"Mileage\"].str.split(\" \", expand = True)\n",
    "mileage_test = X_test[\"Mileage\"].str.split(\" \", expand = True)\n",
    "\n",
    "X_train[\"Mileage\"] = pd.to_numeric(mileage_train[0], errors = 'coerce')\n",
    "X_test[\"Mileage\"] = pd.to_numeric(mileage_test[0], errors = 'coerce')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's check for missing values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "print(sum(X_train[\"Mileage\"].isnull()))\n",
    "print(sum(X_test[\"Mileage\"].isnull()))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There is one missing value in each. I'll replace the missing value with the mean value of the column based on the training data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train[\"Mileage\"].fillna(X_train[\"Mileage\"].astype(\"float64\").mean(), inplace = True)\n",
    "X_test[\"Mileage\"].fillna(X_train[\"Mileage\"].astype(\"float64\").mean(), inplace = True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Engine, Power and Seats\n",
    "\n",
    "The `Engine` values are defined in CC so I need to remove `CC` from the data. Similarly, `Power` has bhp, so I'll remove `bhp` from it. Also, as there are missing values in `Engine`, `Power` and `Seats`, I'll again replace them with the mean."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "cc_train = X_train[\"Engine\"].str.split(\" \", expand = True)\n",
    "cc_test = X_test[\"Engine\"].str.split(\" \", expand = True)\n",
    "X_train[\"Engine\"] = pd.to_numeric(cc_train[0], errors = 'coerce')\n",
    "X_test[\"Engine\"] = pd.to_numeric(cc_test[0], errors = 'coerce')\n",
    "\n",
    "bhp_train = X_train[\"Power\"].str.split(\" \", expand = True)\n",
    "bhp_test = X_test[\"Power\"].str.split(\" \", expand = True)\n",
    "X_train[\"Power\"] = pd.to_numeric(bhp_train[0], errors = 'coerce')\n",
    "X_test[\"Power\"] = pd.to_numeric(bhp_test[0], errors = 'coerce')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train[\"Engine\"].fillna(X_train[\"Engine\"].astype(\"float64\").mean(), inplace = True)\n",
    "X_test[\"Engine\"].fillna(X_train[\"Engine\"].astype(\"float64\").mean(), inplace = True)\n",
    "\n",
    "X_train[\"Power\"].fillna(X_train[\"Power\"].astype(\"float64\").mean(), inplace = True)\n",
    "X_test[\"Power\"].fillna(X_train[\"Power\"].astype(\"float64\").mean(), inplace = True)\n",
    "\n",
    "X_train[\"Seats\"].fillna(X_train[\"Seats\"].astype(\"float64\").mean(), inplace = True)\n",
    "X_test[\"Seats\"].fillna(X_train[\"Seats\"].astype(\"float64\").mean(), inplace = True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### New Price\n",
    "\n",
    "As most of the values are missing, I'll drop this column altogether."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train.drop([\"New_Price\"], axis = 1, inplace = True)\n",
    "X_test.drop([\"New_Price\"], axis = 1, inplace = True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Processing\n",
    "\n",
    "Now that we have worked with the training data, let's create dummy columns for categorical columns before we begin training."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train = pd.get_dummies(X_train,\n",
    "                         columns = [\"Manufacturer\", \"Fuel_Type\", \"Transmission\", \"Owner_Type\"],\n",
    "                         drop_first = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_test = pd.get_dummies(X_test,\n",
    "                         columns = [\"Manufacturer\", \"Fuel_Type\", \"Transmission\", \"Owner_Type\"],\n",
    "                         drop_first = True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It might be possible that the dummy column creation would be different in test and train data, thus, I'd fill in all missing columns with zeros."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "missing_cols = set(X_train.columns) - set(X_test.columns)\n",
    "for col in missing_cols:\n",
    "    X_test[col] = 0\n",
    "X_test = X_test[X_train.columns]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Finally, as the last step of data processing, I'll scale the data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "standardScaler = StandardScaler()\n",
    "standardScaler.fit(X_train)\n",
    "X_train = standardScaler.transform(X_train)\n",
    "X_test = standardScaler.transform(X_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Training and predicting\n",
    "\n",
    "I'll create a **Linear Regression** model and a **Random Forest** model to train on the data and use it for future predictions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7008908549416721"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "linearRegression = LinearRegression()\n",
    "linearRegression.fit(X_train, y_train)\n",
    "y_pred = linearRegression.predict(X_test)\n",
    "r2_score(y_test, y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8860868487769373"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rf = RandomForestRegressor(n_estimators = 100)\n",
    "rf.fit(X_train, y_train)\n",
    "y_pred = rf.predict(X_test)\n",
    "r2_score(y_test, y_pred)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The **Random Forest** model performed the best with a R2 score of **0.88**."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
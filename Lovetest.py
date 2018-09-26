{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Asking for the names\n",
    "name1 = input(\"What is the first name?\")\n",
    "name2 = input(\"What is the second name?\")\n",
    "\n",
    "#Stripping the names of possible Uppercase letters and whitespaces\n",
    "name1 = name1.lower().strip()\n",
    "name2 = name2.lower().strip()\n",
    "\n",
    "#Determining if the names are a good match or not\n",
    "if name1 > name2:\n",
    "    print(\"You are a bad match\")\n",
    "    \n",
    "elif name1 < name2:\n",
    "    print(\"You are a good match\")\n",
    "\n",
    "elif name1 == name2:\n",
    "    print(\"You have the same name\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

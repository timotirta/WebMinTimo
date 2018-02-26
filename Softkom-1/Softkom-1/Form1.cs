﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace Softkom_1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        List<Double[]> data = new List<Double[]>();
        Double alpha = 0.005;
        String[] nama;
        Random rnd = new Random();
        int iter = 0, iteration = 1000;

        int[] y = new int[1600];
        private void Form1_Load(object sender, EventArgs e)
        {
            bool awal = true;
            StreamReader sr = new StreamReader("winequality-red.csv");
            int ctr = 0;
            while (!sr.EndOfStream)
            {
                if (awal)
                {
                    nama = sr.ReadLine().Replace("\"", string.Empty).Split(';');
                    for (int i = 0; i < 1600; i++)
                    {
                        data.Add(new Double[11]);
                    }
                    awal = false;
                }
                else
                {
                    String[] temp = sr.ReadLine().Split(';');
                    for (int i = 0; i < temp.Length; i++)
                    {
                        if (temp.Length - 1 == i)
                            y[ctr] = Convert.ToInt32(temp[i].ToString());
                        else
                            data[ctr][i] = Convert.ToDouble(temp[i].ToString());

                    }
                    ctr++;
                }
            }
            Double[] tetha = { 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 };
            Double[] temptetha = { 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 };
            Double h = new Double();
            //Double[] temph = new Double[data.Count];
            /*for (int i = 0; i < tetha.Length; i++)
            {
                tetha[i] = rnd.NextDouble();
            }*/
            while (iter < iteration)
            {
                h = 0;
                for (int i = 0; i < data.Count; i++)
                {
                    for (int j = 0; j < data[i].Length; j++)
                    {
                        h += (data[i][j] * tetha[j]);
                    }
                    for (int j = 0; j < 11; j++)
                    {
                        temptetha[j] = tetha[j] - alpha * (h - y[i]) * data[i][j];
                        Console.WriteLine(temptetha[0]);
                    }
                    for (int j = 0; j < 11; j++)
                    {
                        tetha[j] = temptetha[j];
                    }
                }
                //Console.WriteLine(temptetha[0]);
                Console.WriteLine(tetha[0]);
                //Console.WriteLine(h.ToString());
                iter++;
            }
            //MessageBox.Show("H(x) = " + tetha[0] + " x0 " + tetha[1] + " x1 " + tetha[2] + " x2 " + tetha[3] + " x3 " + tetha[4] + " x4 " + tetha[5] + " x5 " + tetha[6] + " x6 " + tetha[7] + " x7 " + tetha[8] + " x8 " + tetha[9] + " x9 " + tetha[10] + " x10");
            Double[] xku = { 7.4, 0.7, 0, 1.9, 0.076, 11, 34, 0.9978, 3.51, 0.56, 9.4 };
            Double hasil = 0;
            for (int i = 0; i < xku.Length; i++)
            {
                hasil += tetha[i] * xku[i];
            }
            MessageBox.Show("H = "+Convert.ToInt32(hasil));
        }
    }
}

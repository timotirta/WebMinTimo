using System;
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
        Double alpha = 0.0003;
        String[] nama;
        Random rnd = new Random();
        int iter = 1, iteration = 1000;
        Double[] y = new Double[1600];
        Double[] min = new Double[11];
        Double[] max = new Double[11];
        public void loadData()
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
                            y[ctr] = Convert.ToDouble(temp[i].ToString());
                        else
                            data[ctr][i] = Convert.ToDouble(temp[i].ToString());

                    }
                    ctr++;
                }
            }
            sr.Close();
            for (int i = 0; i < 1600; i++)
            {
                for (int j = 0; j < 11; j++)
                {
                    min[j] = min[j] > data[i][j] ? data[i][j] : min[j];
                    max[j] = max[j] < data[i][j] ? data[i][j] : max[j];
                }
            }
        }
        public void saveTetha()
        {
            StreamWriter sw = new StreamWriter("savetet.txt");
            sw.WriteLine(tetha[0] + ";" + tetha[1] + ";" + tetha[2] + ";" + tetha[3] + ";" + tetha[4] + ";" + tetha[5] + ";" + tetha[6] + ";" + tetha[7] + ";" + tetha[8] + ";" + tetha[9] + ";" + tetha[10]);
            sw.Close();
        }
        public void loadTetha()
        {
            String[] temp;
            StreamReader sr = new StreamReader("savetet.txt");
            temp = sr.ReadLine().Split(';');
            for (int i = 0; i < 11; i++)
            {
                tetha[i] = Convert.ToDouble(temp[i]);
            }
            sr.Close();
        }
        Double[] tetha = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
        Double[] temptetha = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
        Double h = 0.0;
        Timer tku = new Timer();
        List<Double> cfHasil = new List<Double>();
        public void train()
        {
            if (iter < iteration)
            {
                Console.WriteLine("Iterasi - " + iter);
                Console.WriteLine("-------------------------------------------------");
                Double hasilku = 0.0;
                for (int i = 0; i < data.Count; i++)
                {
                    h = 0;
                    for (int j = 0; j < data[i].Length; j++)
                    {
                        h += (data[i][j] * tetha[j]);
                    }
                    for (int j = 0; j < 11; j++)
                    {
                        temptetha[j] = tetha[j] - (alpha * (((h - y[i]) * data[i][j]) / (data.Count * 2)));
                        //Console.WriteLine(temptetha[0]);
                    }
                    for (int j = 0; j < 11; j++)
                    {
                        hasilku += (h - y[i]) * (h - y[i]);
                        //Console.WriteLine(temptetha[0]);
                    }
                    for (int j = 0; j < 11; j++)
                    {
                        tetha[j] = temptetha[j];
                    }
                }
                hasilku /= 11.0;
                hasilku /= data.Count * 2;
                chart1.Series["CostFunction"].Points.AddXY(iter + "", hasilku);
                //if (hasilku <= 0) iter = iteration;
                //Console.WriteLine(temptetha[0]);
                //Console.WriteLine(tetha[0]);
                //Console.WriteLine(h.ToString());
                Console.WriteLine(hasilku);
                numericUpDown33.Value = (decimal)tetha[0];
                numericUpDown32.Value = (decimal)tetha[1];
                numericUpDown31.Value = (decimal)tetha[2];
                numericUpDown30.Value = (decimal)tetha[3];
                numericUpDown29.Value = (decimal)tetha[4];
                numericUpDown28.Value = (decimal)tetha[5];
                numericUpDown27.Value = (decimal)tetha[6];
                numericUpDown26.Value = (decimal)tetha[7];
                numericUpDown25.Value = (decimal)tetha[8];
                numericUpDown24.Value = (decimal)tetha[9];
                numericUpDown12.Value = (decimal)tetha[10];
                iter++;
                saveTetha();
                //Console.WriteLine("H(x) = " + tetha[0] + " x0 " + tetha[1] + " x1 " + tetha[2] + " x2 " + tetha[3] + " x3 " + tetha[4] + " x4 " + tetha[5] + " x5 " + tetha[6] + " x6 " + tetha[7] + " x7 " + tetha[8] + " x8 " + tetha[9] + " x9 " + tetha[10] + " x10");
            }
            else
            {
                tku.Stop();
                tampilkan();
                saveTetha();
            }
        }
        void timer1_Tick(object sender, EventArgs e)
        {
            train();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            //loadTetha();
            loadData();
            //normalisasi
            for (int i = 0; i < data.Count; i++)
            {
                for (int j = 0; j < 11; j++)
                {
                    data[i][j] = (data[i][j] - min[j]) / (max[j] - min[j]);
                }
            }
            tku.Interval = 1;
            tku.Tick += new EventHandler(timer1_Tick);
        }
        bool awalan = true;
        private void button1_Click(object sender, EventArgs e)
        {
            alpha = Convert.ToDouble(numericAlpha.Value);
            if (awalan)
            {
                tetha[0] = Convert.ToDouble(numericUpDown1.Value);
                tetha[1] = Convert.ToDouble(numericUpDown2.Value);
                tetha[2] = Convert.ToDouble(numericUpDown3.Value);
                tetha[3] = Convert.ToDouble(numericUpDown4.Value);
                tetha[4] = Convert.ToDouble(numericUpDown5.Value);
                tetha[5] = Convert.ToDouble(numericUpDown6.Value);
                tetha[6] = Convert.ToDouble(numericUpDown7.Value);
                tetha[7] = Convert.ToDouble(numericUpDown8.Value);
                tetha[8] = Convert.ToDouble(numericUpDown9.Value);
                tetha[9] = Convert.ToDouble(numericUpDown10.Value);
                tetha[10] = Convert.ToDouble(numericUpDown11.Value);
                iter = 0;
                iteration = Convert.ToInt32(numericIterasi.Value);
                awalan = false;
            }
            else
            {
                iteration += Convert.ToInt32(numericIterasi.Value);
            }
            tku.Start();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Double hasil = 0;
            Double[] xku1 = new Double[11];
            xku1[0] = Convert.ToDouble(numericUpDown23.Value);
            xku1[1] = Convert.ToDouble(numericUpDown22.Value);
            xku1[2] = Convert.ToDouble(numericUpDown21.Value);
            xku1[3] = Convert.ToDouble(numericUpDown20.Value);
            xku1[4] = Convert.ToDouble(numericUpDown19.Value);
            xku1[5] = Convert.ToDouble(numericUpDown18.Value);
            xku1[6] = Convert.ToDouble(numericUpDown17.Value);
            xku1[7] = Convert.ToDouble(numericUpDown16.Value);
            xku1[8] = Convert.ToDouble(numericUpDown15.Value);
            xku1[9] = Convert.ToDouble(numericUpDown14.Value);
            xku1[10] = Convert.ToDouble(numericUpDown13.Value);
            for (int i = 0; i < 11; i++)
            {
                hasil += tetha[i] * xku1[i];
            }
            hasil = hasil < 0 ? 0 : hasil;
            hasil = hasil > 10 ? 10 : hasil;
            numericPredict.Value = (decimal)hasil;
        }
        public void tampilkan()
        {
            //MessageBox.Show("H(x) = " + tetha[0] + " x0 " + tetha[1] + " x1 " + tetha[2] + " x2 " + tetha[3] + " x3 " + tetha[4] + " x4 " + tetha[5] + " x5 " + tetha[6] + " x6 " + tetha[7] + " x7 " + tetha[8] + " x8 " + tetha[9] + " x9 " + tetha[10] + " x10");
            Double[] xku1 = { 7.9, 0.32, 0.51, 1.8, 0.341, 17, 56, 0.9969, 3.04, 1.08, 9.2, 6 };
            Double hasil = 0;
            for (int i = 0; i < 11; i++)
            {
                hasil += tetha[i] * xku1[i];
            }
                Console.WriteLine("H = " + hasil);
                Console.WriteLine("Asli = " + xku1[11]);
                Console.WriteLine("Beda = " + (hasil - xku1[11]));
        }
    }
}

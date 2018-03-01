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
        Double alpha = 0.6;
        String[] nama;
        Random rnd = new Random();
        int iter = 1, iteration = 1000;
        Double[] y = new Double[1600];
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
        Double[] tetha = { 0,0,0,0,0,0,0,0,0,0,0,0 };
        Double[] temptetha = { 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 };
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
                        hasilku += ((h - y[i]) * data[i][j]) / (1599 * 2);
                        //Console.WriteLine(temptetha[0]);
                    }
                    for (int j = 0; j < 11; j++)
                    {
                        tetha[j] = temptetha[j];
                    }
                }
                hasilku /= 11.0;
                chart1.Series["Hnya"].Points.AddXY(iter + "", hasilku);
                //if (hasilku <= 0) iter = iteration;
                //Console.WriteLine(temptetha[0]);
                //Console.WriteLine(tetha[0]);
                //Console.WriteLine(h.ToString());
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
            tku.Interval = 1;
            tku.Tick += new EventHandler(timer1_Tick);
            tku.Start();
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
            if (hasil == xku1[11])
            {
                Console.WriteLine("Benar");
            }
            else
            {
                Console.WriteLine("H = " + hasil);
                Console.WriteLine("Asli = " + xku1[11]);
                Console.WriteLine("Salah! Beda = " + (hasil - xku1[11]));
            }
        }
    }
}

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
        private void Form1_Load(object sender, EventArgs e)
        {
            bool awal = true;
            StreamReader sr = new StreamReader("winequality-red.csv");
            int ctr = 0;
            String[] nama;
            int[] y = new int[1600];
            while (!sr.EndOfStream)
            {
                if (awal)
                {
                    nama = sr.ReadLine().Replace("\"", string.Empty).Split(';');
                    for (int i = 0; i < 1600; i++)
                    {
                        data.Add(new Double[12]);
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
            Double[] tetha = new Double[11];
            Double[] temptetha = new Double[11];
        }
    }
}

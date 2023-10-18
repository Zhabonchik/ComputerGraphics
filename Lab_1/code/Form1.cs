using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Lab_1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void R_Trackbar_Scroll(object sender, EventArgs e)
        {
            R = R_Trackbar.Value;
            //convertation
            convert_RGB_CMYK();
            convert_RGB_HSV();
            update_info();
        }
        private void G_Trackbar_Scroll(object sender, EventArgs e)
        {
            G = G_Trackbar.Value;
            //convertation
            convert_RGB_CMYK();
            convert_RGB_HSV();
            update_info();
        }
        private void B_Trackbar_Scroll(object sender, EventArgs e)
        {
            B = B_Trackbar.Value;
            //convertation
            convert_RGB_CMYK();
            convert_RGB_HSV();
            update_info();
        }
        private void C_Trackbar_Scroll(object sender, EventArgs e)
        {
            C = C_Trackbar.Value;
            //convertation
            convert_CMYK_RGB();
            convert_RGB_HSV();
            //setting panel values
            update_info();
        }

        private void M_Trackbar_Scroll(object sender, EventArgs e)
        {
            M = M_Trackbar.Value;
            //convertation
            convert_CMYK_RGB();
            convert_RGB_HSV();
            update_info();
        }

        private void Y_Trackbar_Scroll(object sender, EventArgs e)
        {
            Y = Y_Trackbar.Value;
            //convertation
            convert_CMYK_RGB();
            convert_RGB_HSV();
            update_info();
        }

        private void K_Trackbar_Scroll(object sender, EventArgs e)
        {
            K = K_Trackbar.Value;
            //convertation
            convert_CMYK_RGB();
            convert_RGB_HSV();
            update_info();
        }
        private void H_Trackbar_Scroll(object sender, EventArgs e)
        {
            H = H_Trackbar.Value;
            //convertation
            convert_HSV_RGB();
            convert_RGB_CMYK();
            update_info();
        }

        private void S_Trackbar_Scroll(object sender, EventArgs e)
        {
            S = S_Trackbar.Value;
            //convertation
            convert_HSV_RGB();
            convert_RGB_CMYK();
            update_info();
        }

        private void V_Trackbar_Scroll(object sender, EventArgs e)
        {
            V = V_Trackbar.Value;
            //convertation
            convert_HSV_RGB();
            convert_RGB_CMYK();
            update_info();
        }
        private void R_Textbox_TextChanged(object sender, EventArgs e)
        {
            R = Int32.Parse(R_Textbox.Text);
            //convertation
            convert_RGB_CMYK();
            convert_RGB_HSV();
            update_info();
        }

        private void G_Textbox_TextChanged(object sender, EventArgs e)
        {
            G = Int32.Parse(G_Textbox.Text);
            //convertation
            convert_RGB_CMYK();
            convert_RGB_HSV();
            update_info();
        }

        private void B_Textbox_TextChanged(object sender, EventArgs e)
        {
            B = Int32.Parse(B_Textbox.Text);
            //convertation
            convert_RGB_CMYK();
            convert_RGB_HSV();
            update_info();
        }
        private void C_Textbox_TextChanged(object sender, EventArgs e)
        {
            C = Int32.Parse(C_Textbox.Text);
            //convertation
            convert_CMYK_RGB();
            convert_RGB_HSV();
            update_info();
        }

        private void M_Textbox_TextChanged(object sender, EventArgs e)
        {
            M = Int32.Parse(M_Textbox.Text);
            //convertation
            convert_CMYK_RGB();
            convert_RGB_HSV();
            update_info();
        }

        private void Y_Textbox_TextChanged(object sender, EventArgs e)
        {
            Y = Int32.Parse(Y_Textbox.Text);
            //convertation
            convert_CMYK_RGB();
            convert_RGB_HSV();
            update_info();
        }

        private void K_Textbox_TextChanged(object sender, EventArgs e)
        {
            K = Int32.Parse(K_Textbox.Text);
            //convertation
            convert_CMYK_RGB();
            convert_RGB_HSV();
            update_info();
        }
        private void H_Textbox_TextChanged(object sender, EventArgs e)
        {
            H = Int32.Parse(H_Textbox.Text);
            //convertation
            convert_HSV_RGB();
            convert_RGB_CMYK();
            update_info();
        }

        private void S_Textbox_TextChanged(object sender, EventArgs e)
        {
            S = Int32.Parse(S_Textbox.Text);
            //convertation
            convert_HSV_RGB();
            convert_RGB_CMYK();
            update_info();
        }

        private void V_Textbox_TextChanged(object sender, EventArgs e)
        {
            V = Int32.Parse(V_Textbox.Text);
            //convertation
            convert_HSV_RGB();
            convert_RGB_CMYK();
            update_info();
        }
        private void update_info()
        {
            //setting panel values
            set_RGB_Panel_Color();
            set_CMYK_Panel_Color();
            set_HSV_Panel_Color();
            //setting TextBox values
            set_RGB_Label_Values();
            set_CMYK_Label_Values();
            set_HSV_Label_Values();
            //setting TrackBar values
            set_RGB_Trackbar_Values();
            set_CMYK_Trackbar_Values();
            set_HSV_Trackbar_Values();
        }
        private void set_RGB_Panel_Color()
        {
            RBG_Panel.BackColor = Color.FromArgb(R, G, B);
        }
        private void set_CMYK_Panel_Color()
        {
            CMYK_Panel.BackColor = Color.FromArgb(R, G, B);
        }
        private void set_HSV_Panel_Color()
        {
            HSV_Panel.BackColor = Color.FromArgb(R, G, B);
        }
        private void convert_RGB_CMYK()
        {
            K = (int)Math.Min(Math.Min(100 - 100 * ((float)R / 255), 100 - 100 * ((float)G / 255)), 100 - 100 * ((float)B / 255));
            if (K == 100)
            {
                C = 0;
                M = 0;
                K = 0;
            } else
            {
                C = (int)(100 * (100 - 100 * ((float)R / 255) - K) / (100 - K));
                M = (int)(100 * (100 - 100 * ((float)G / 255) - K) / (100 - K));
                Y = (int)(100 * (100 - 100 * ((float)B / 255) - K) / (100 - K));
            }

        }
        private void convert_RGB_HSV()
        {
            float r = (float)R / 255;
            float g = (float)G / 255;
            float b = (float)B / 255;
            float c_max = Math.Max(Math.Max(r, g), b);
            float c_min = Math.Min(Math.Min(r, g), b);
            float delta = c_max - c_min;
            V = (int)(c_max * 100);
            if (delta == 0)
            {
                H = 0;
            }
            else if (c_max == r)
            {
                H = (int)(60 * ((Math.Abs(g - b) / delta) % 6));
            }
            else if (c_max == g)
            {
                H = (int)(60 * ((Math.Abs(b - r) / delta) + 2));
            }
            else
            {
                H = (int)(60 * ((Math.Abs(r - g) / delta) + 4));
            }
            if (c_max == 0)
            {
                S = 0;
            }
            else
            {
                S = (int)(100 * delta / c_max);
            }
        }
        private void convert_HSV_RGB()
        {
            float c = (float)V * S / 10000;
            float x = c * (1 - Math.Abs((H / 60) % 2 - 1));
            float m = (float)V / 100 - c;
            float r = 0, g = 0, b = 0;
            if(0 <= H && H < 60 || H == 360)
            {
                r = c;
                g = x;
                b = 0;
            } else if (60 <= H && H < 120)
            {
                r = x;
                g = c;
                b = 0;
            } else if(120 <= H && H < 180)
            {
                r = 0;
                g = c;
                b = x;
            } else if(180 <= H && H < 240)
            {
                r = 0;
                g = x;
                b = c;
            } else if (240 <= H && H < 300)
            {
                r = x;
                g = 0;
                b = c;
            } else if (300 <= H && H < 360)
            {
                r = c;
                g = 0;
                b = x;
            }
            R = (int)((r + m) * 255);
            G = (int)((g + m) * 255);
            B = (int)((b + m) * 255);
        }
        private void convert_CMYK_RGB()
        {
            R = (int)(255 * (1 - (float)C / 100)*(1 - (float)K / 100));
            G = (int)(255 * (1 - (float)M / 100) * (1 - (float)K / 100));
            B = (int)(255 * (1 - (float)Y / 100) * (1 - (float)K / 100));
        }
        private void set_RGB_Label_Values()
        {
            R_Label.Text = R.ToString();
            G_Label.Text = G.ToString();
            B_Label.Text = B.ToString();
        }
        private void set_HSV_Label_Values()
        {
            H_Label.Text = H.ToString();
            S_Label.Text = S.ToString();
            V_Label.Text = V.ToString();
        }
        private void set_CMYK_Label_Values()
        {
            C_Label.Text = C.ToString();
            M_Label.Text = M.ToString();
            Y_Label.Text = Y.ToString();
            K_Label.Text = K.ToString();
        }
        private void set_RGB_Trackbar_Values()
        {
            R_Trackbar.Value = R;
            G_Trackbar.Value = G;
            B_Trackbar.Value = B;
        }
        private void set_CMYK_Trackbar_Values()
        {
            C_Trackbar.Value = C;
            M_Trackbar.Value = M;
            Y_Trackbar.Value = Y;
            K_Trackbar.Value = K;
        }
        private void set_HSV_Trackbar_Values()
        {
            H_Trackbar.Value = H;
            S_Trackbar.Value = S;
            V_Trackbar.Value = V;
        }
        private int R = 0;
        private int G = 0;
        private int B = 0;
        private int C = 0;
        private int M = 0;
        private int Y = 0;
        private int K = 0;
        private int H = 0;
        private int V = 0;
        private int S = 0;

        private void button1_Click(object sender, EventArgs e)
        {
            ColorDialog colorDialog = new ColorDialog();
            colorDialog1.Color = this.BackColor;
            colorDialog.AllowFullOpen = true;
            colorDialog.ShowDialog();
            R = colorDialog.Color.R;
            G = colorDialog.Color.G;
            B = colorDialog.Color.B;
            convert_RGB_CMYK();
            convert_RGB_HSV();
            update_info();
        }
    }
}

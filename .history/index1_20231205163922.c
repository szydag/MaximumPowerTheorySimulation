#include <stdio.h>
#include <math.h>

struct guc_kaynagi {
    float gerilim;
    float ic_direnc;
};

float guc_hesapla(float Ri, float Rl, float Vi)
{
    float sonuc, guc;
    guc=((Rl*Rl)*Vi)/(Rl+Ri);
    sonuc= guc;
    return sonuc;
}

float kayip_guc_hesapla (float Ri, float Rl, float Vi)
{
    float sonuc, guc;
    guc=((Ri*Ri)*Vi)/(Rl+Ri);
    sonuc= guc;
    return sonuc;

}

int main()
{
    float Vi, Ri, Pl, Pi, Rl_sayac, fark;
    struct guc_kaynagi deney1;
    printf ("\n Guc kaynagi gerilimini giriniz");
    scanf ("%f", &Vi);
    printf ("\n Guc kaynagi direncini giriniz");
    scanf ("%f", &Ri);
    deney1.gerilim=Vi;
    deney1.ic_direnc=Ri;
    Rl_sayac=0;
    while (Rl_sayac < 500) {
        Pl=guc_hesapla(deney1.ic_direnc,Rl_sayac,deney1.gerilim);
        Pi=kayip_guc_hesapla(deney1.ic_direnc,Rl_sayac,deney1.gerilim);
        fark=Pl-Pi;

        printf("Rl = %f icin \n harcanan guc: %f \n kayip guc: %f \n fark: %f \n ", Rl_sayac, Pl,  Pi, fark);
        Rl_sayac = Rl_sayac + 5;
    }
}
import React, { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Checkbox } from "@/components/ui/checkbox";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogFooter,
} from "@/components/ui/dialog";
import { Badge } from "@/components/ui/badge";
import {
  FileText,
  Copy,
  Trash2,
  CheckCircle,
  ClipboardList,
  Heart,
  Wind,
  Stethoscope,
  Pill,
} from "lucide-react";

const MOTIVOS_GRUPOS = [
  {
    grupo: "Hérnias da Parede Abdominal",
    opcoes: [
      "Hérnia Inguinal Direita",
      "Hérnia Inguinal Esquerda",
      "Hérnia Inguinal Bilateral",
      "Hérnia Inguinal Direita Recidivada",
      "Hérnia Inguinal Esquerda Recidivada",
      "Hérnia Inguinal Bilateral Recidivada",
      "Hérnia Crural Direita",
      "Hérnia Crural Esquerda",
      "Hérnia Crural Bilateral",
      "Hérnia Umbilical",
      "Hérnia Umbilical Recidivada",
      "Hérnia Epigástrica",
      "Hérnia Epigástrica Recidivada",
      "Hérnia Incisional",
      "Hérnia Incisional Recidivada",
      "Hérnia de Spiegel",
      "Hérnia Lombar",
      "Hérnia Obturadora",
      "Hérnia Paraesofágica / Hiatal",
      "Diástase dos Retos Abdominais",
    ],
  },
  {
    grupo: "Vesícula e Vias Biliares",
    opcoes: [
      "Colelitíase / Colecistite Crônica Calculosa",
      "Colecistite Aguda (eletiva após resolução)",
      "Coledocolitíase",
      "Pólipo de Vesícula Biliar",
      "Colangite Crônica",
    ],
  },
  {
    grupo: "Esôfago e Estômago",
    opcoes: [
      "Doença do Refluxo Gastroesofágico (DRGE) — Fundoplicatura",
      "Hérnia Hiatal Mista / Paraesofágica",
      "Acalasia de Esôfago",
      "Divertículo de Zenker",
      "Divertículo Esofágico de Tração",
      "Úlcera Péptica Gástrica Refratária",
      "Úlcera Péptica Duodenal Refratária",
      "Tumor Benigno Gástrico (GIST / Leiomioma)",
      "Estenose Pilórica do Adulto",
    ],
  },
  {
    grupo: "Intestino Delgado",
    opcoes: [
      "Aderências / Bridas Intestinais (cirurgia eletiva)",
      "Tumor Benigno de Intestino Delgado",
      "Doença de Crohn — Ressecção Eletiva",
      "Divertículo de Meckel Sintomático",
      "Fístula Enterocutânea",
    ],
  },
  {
    grupo: "Cólon e Reto",
    opcoes: [
      "Doença Diverticular do Cólon Sintomática",
      "Pólipo Colônico de Grande Volume (não ressecável por colonoscopia)",
      "Megacólon Chagásico",
      "Constipação Crônica de Causa Colônica",
      "Colite Ulcerativa — Cirurgia Eletiva",
      "Doença de Crohn Colônica — Cirurgia Eletiva",
      "Prolapso Retal",
      "Retocele Sintomática",
      "Estenose Retal Benigna",
    ],
  },
  {
    grupo: "Região Anorretal e Períneo",
    opcoes: [
      "Hemorróidas Grau III / IV",
      "Fissura Anal Crônica",
      "Fístula Perianal (transesfincteriana / supraesfincteriana)",
      "Fístula Perianal Baixa (interesfincteriana / submucosa)",
      "Abscesso Anorretal Recorrente",
      "Cisto Pilonidal / Seio Pilonidal",
      "Condiloma Acuminado Perianal (extenso)",
      "Incontinência Fecal — Esfincteroplastia Eletiva",
      "Hidradenite Supurativa Perianal",
    ],
  },
  {
    grupo: "Fígado, Pâncreas e Baço",
    opcoes: [
      "Cisto Hepático Simples Sintomático",
      "Cisto Hidático Hepático",
      "Hepatolitíase",
      "Hemangioma Hepático Sintomático",
      "Adenoma Hepático",
      "Hipertensão Portal — Shunt Cirúrgico Eletivo",
      "Pancreatite Crônica — Cirurgia Eletiva (Frey / Puestow / Beger)",
      "Pseudocisto Pancreático Sintomático",
      "Cistoadenoma Seroso / Mucinoso do Pâncreas",
      "Esplenomegalia — Esplenectomia Eletiva",
      "Cisto Esplênico Sintomático",
    ],
  },
  {
    grupo: "Tireoide e Paratireoide",
    opcoes: [
      "Bócio Nodular — Tireoidectomia Parcial / Total",
      "Nódulo de Tireoide Indeterminado (Bethesda III / IV)",
      "Hipertireoidismo Refratário ao Tratamento Clínico",
      "Hiperparatireoidismo Primário — Paratireoidectomia",
      "Adenoma de Paratireoide",
    ],
  },
  {
    grupo: "Parede Torácica e Mediastino (Cirurgia Geral)",
    opcoes: [
      "Empiema Pleural Crônico (decorticação eletiva)",
      "Cisto Mediastinal Benigno",
      "Tumor de Parede Torácica Benigno",
    ],
  },
  {
    grupo: "Mama (Cirurgia Geral)",
    opcoes: [
      "Fibroadenoma de Mama",
      "Tumor Filodes Benigno de Mama",
      "Ginecomastia",
      "Abscesso Mamário Recorrente / Fístula de Ducto",
      "Cisto Mamário Volumoso / Recorrente",
    ],
  },
  {
    grupo: "Partes Moles e Dermatologia",
    opcoes: [
      "Cisto Sebáceo / Epidérmico",
      "Lipoma",
      "Fibroma / Dermatofibroma",
      "Nevo Melanocítico — Exérese Eletiva",
      "Queratose Seborreica Complicada",
      "Granuloma Piogênico",
      "Carcinoma Basocelular / Espinocelular (ressecção eletiva)",
      "Cirurgia Ambulatorial Dermatológica Geral",
    ],
  },
  {
    grupo: "Outros",
    opcoes: [
      "Outro (especificar no campo personalizado)",
    ],
  },
];

// Lista plana para compatibilidade com o campo de texto gerado
const MOTIVOS = MOTIVOS_GRUPOS.flatMap((g) => g.opcoes);

const PROCEDIMENTOS_POR_MOTIVO = {
  "Hérnia Inguinal Direita": [
    "Herniorrafia inguinal direita com tela — técnica de Lichtenstein (aberta)",
    "Herniorrafia inguinal direita laparoscópica — TAPP (transabdominal pré-peritoneal)",
    "Herniorrafia inguinal direita laparoscópica — TEP (totalmente extraperitoneal)",
    "Herniorrafia inguinal direita robótica (TAPP robótico)",
    "Herniorrafia inguinal direita sem tela — técnica de Shouldice (aberta)",
  ],
  "Hérnia Inguinal Esquerda": [
    "Herniorrafia inguinal esquerda com tela — técnica de Lichtenstein (aberta)",
    "Herniorrafia inguinal esquerda laparoscópica — TAPP",
    "Herniorrafia inguinal esquerda laparoscópica — TEP",
    "Herniorrafia inguinal esquerda robótica (TAPP robótico)",
    "Herniorrafia inguinal esquerda sem tela — técnica de Shouldice",
  ],
  "Hérnia Inguinal Bilateral": [
    "Herniorrafia inguinal bilateral com tela — técnica de Lichtenstein bilateral (aberta)",
    "Herniorrafia inguinal bilateral laparoscópica — TAPP bilateral",
    "Herniorrafia inguinal bilateral laparoscópica — TEP bilateral",
    "Herniorrafia inguinal bilateral robótica",
  ],
  "Hérnia Inguinal Direita Recidivada": [
    "Herniorrafia inguinal direita recidivada — TAPP laparoscópico (acesso pré-peritoneal)",
    "Herniorrafia inguinal direita recidivada — TEP laparoscópico",
    "Herniorrafia inguinal direita recidivada com tela — abordagem pré-peritoneal aberta (Stoppa / Kugel)",
    "Herniorrafia inguinal direita recidivada robótica",
  ],
  "Hérnia Inguinal Esquerda Recidivada": [
    "Herniorrafia inguinal esquerda recidivada — TAPP laparoscópico",
    "Herniorrafia inguinal esquerda recidivada — TEP laparoscópico",
    "Herniorrafia inguinal esquerda recidivada com tela — abordagem pré-peritoneal aberta",
    "Herniorrafia inguinal esquerda recidivada robótica",
  ],
  "Hérnia Inguinal Bilateral Recidivada": [
    "Herniorrafia inguinal bilateral recidivada — TAPP bilateral laparoscópico",
    "Herniorrafia inguinal bilateral recidivada — TEP bilateral",
    "Herniorrafia inguinal bilateral recidivada robótica",
  ],
  "Hérnia Crural Direita": [
    "Herniorrafia crural direita com tela — acesso inguinal (aberta)",
    "Herniorrafia crural direita laparoscópica — TAPP",
    "Herniorrafia crural direita — acesso pré-peritoneal (Nyhus / Stoppa)",
  ],
  "Hérnia Crural Esquerda": [
    "Herniorrafia crural esquerda com tela — acesso inguinal (aberta)",
    "Herniorrafia crural esquerda laparoscópica — TAPP",
    "Herniorrafia crural esquerda — acesso pré-peritoneal (Nyhus / Stoppa)",
  ],
  "Hérnia Crural Bilateral": [
    "Herniorrafia crural bilateral com tela — aberta bilateral",
    "Herniorrafia crural bilateral laparoscópica — TAPP bilateral",
  ],
  "Hérnia Umbilical": [
    "Herniorrafia umbilical com tela (aberta — Mayo modificado com tela)",
    "Herniorrafia umbilical laparoscópica — IPOM (intraperitoneal onlay mesh)",
    "Herniorrafia umbilical robótica",
    "Herniorrafia umbilical sutura primária — defeito < 2 cm (sem tela)",
  ],
  "Hérnia Umbilical Recidivada": [
    "Herniorrafia umbilical recidivada com tela — IPOM laparoscópico",
    "Herniorrafia umbilical recidivada — IPOM robótico",
    "Herniorrafia umbilical recidivada aberta com tela pré-peritoneal",
  ],
  "Hérnia Epigástrica": [
    "Herniorrafia epigástrica com tela (aberta)",
    "Herniorrafia epigástrica laparoscópica — IPOM",
    "Herniorrafia epigástrica sutura primária — defeito pequeno",
  ],
  "Hérnia Epigástrica Recidivada": [
    "Herniorrafia epigástrica recidivada com tela — IPOM laparoscópico",
    "Herniorrafia epigástrica recidivada aberta com tela",
  ],
  "Hérnia Incisional": [
    "Hernioplastia incisional com tela — IPOM laparoscópico",
    "Hernioplastia incisional com tela — IPOM robótico",
    "Hernioplastia incisional aberta com tela (onlay / sublay / inlay)",
    "Hernioplastia incisional com tela — eTEP (extraperitoneal endoscópico)",
    "Hernioplastia incisional com separação de componentes (técnica de Ramirez)",
  ],
  "Hérnia Incisional Recidivada": [
    "Hernioplastia incisional recidivada — IPOM laparoscópico",
    "Hernioplastia incisional recidivada — IPOM robótico",
    "Hernioplastia incisional recidivada com separação de componentes",
  ],
  "Hérnia de Spiegel": [
    "Herniorrafia de Spiegel com tela — laparoscópica (IPOM / TAPP)",
    "Herniorrafia de Spiegel com tela — aberta",
  ],
  "Hérnia Lombar": [
    "Herniorrafia lombar com tela — laparoscópica",
    "Herniorrafia lombar com tela — aberta",
  ],
  "Hérnia Obturadora": [
    "Herniorrafia obturadora laparoscópica — TAPP",
    "Herniorrafia obturadora aberta — acesso inguinal ou extraperitoneal",
  ],
  "Hérnia Paraesofágica / Hiatal": [
    "Correção de hérnia hiatal paraesofágica por videolaparoscopia com fundoplicatura de Nissen (360°)",
    "Correção de hérnia hiatal paraesofágica por videolaparoscopia com fundoplicatura de Toupet (270°)",
    "Correção de hérnia hiatal por videolaparoscopia com fundoplicatura de Dor (180° anterior)",
    "Correção de hérnia hiatal robótica com fundoplicatura",
  ],
  "Diástase dos Retos Abdominais": [
    "Correção de diástase dos retos abdominais com plicatura de bainha anterior e tela (aberta)",
    "Correção de diástase dos retos abdominais laparoscópica com tela (eTEP / MILOS)",
    "Correção de diástase dos retos abdominais robótica com tela",
  ],
  "Colelitíase / Colecistite Crônica Calculosa": [
    "Colecistectomia videolaparoscópica eletiva",
    "Colecistectomia robótica eletiva",
    "Colecistectomia aberta (laparotomia subcostal direita)",
    "Colecistectomia laparoscópica com colangiografia intraoperatória",
  ],
  "Colecistite Aguda (eletiva após resolução)": [
    "Colecistectomia videolaparoscópica eletiva (6–8 semanas após resolução)",
    "Colecistectomia aberta eletiva",
  ],
  "Coledocolitíase": [
    "CPRE (colangiopancreatografia retrógrada endoscópica) + colecistectomia laparoscópica",
    "Colecistectomia laparoscópica com exploração laparoscópica do colédoco",
    "Colecistectomia aberta com coledocolitotomia e drenagem em T",
  ],
  "Pólipo de Vesícula Biliar": [
    "Colecistectomia videolaparoscópica (pólipo ≥ 10 mm ou crescimento progressivo)",
    "Colecistectomia aberta (suspeita de malignidade)",
  ],
  "Colangite Crônica": [
    "Colecistectomia videolaparoscópica com exploração das vias biliares",
    "Colecistectomia aberta com coledocolitotomia",
  ],
  "Doença do Refluxo Gastroesofágico (DRGE) — Fundoplicatura": [
    "Fundoplicatura à Nissen (360°) por videolaparoscopia",
    "Fundoplicatura de Toupet (270° posterior) por videolaparoscopia",
    "Fundoplicatura de Dor (180° anterior) por videolaparoscopia",
    "Fundoplicatura robótica (Nissen / Toupet)",
    "Fundoplicatura com correção de hérnia hiatal associada",
  ],
  "Hérnia Hiatal Mista / Paraesofágica": [
    "Correção de hérnia hiatal mista com fundoplicatura de Nissen — videolaparoscopia",
    "Correção de hérnia hiatal mista com fundoplicatura de Toupet — videolaparoscopia",
    "Correção de hérnia hiatal robótica com fundoplicatura",
  ],
  "Acalasia de Esôfago": [
    "Cardiomiotomia de Heller com fundoplicatura parcial — videolaparoscopia",
    "Cardiomiotomia de Heller robótica com fundoplicatura parcial",
    "POEM (miotomia endoscópica oral por via endoscópica)",
  ],
  "Divertículo de Zenker": [
    "Diverticulotomia endoscópica de Zenker (diverticuloscópio / stapler endoscópico)",
    "Diverticulectomia de Zenker cirúrgica (acesso cervical com miotomia do cricofaríngeo)",
  ],
  "Divertículo Esofágico de Tração": [
    "Diverticulectomia esofágica por toracoscopia (VATS)",
    "Diverticulectomia esofágica por toracotomia aberta",
  ],
  "Úlcera Péptica Gástrica Refratária": [
    "Gastrectomia parcial com reconstrução Billroth I (gastroduodenostomia)",
    "Gastrectomia parcial com reconstrução Billroth II (gastrojejunostomia)",
    "Gastrectomia parcial com reconstrução em Y de Roux",
    "Gastrectomia parcial laparoscópica",
  ],
  "Úlcera Péptica Duodenal Refratária": [
    "Vagotomia troncular com piloroplastia (Heineke-Mikulicz)",
    "Vagotomia superseletiva (células parietais)",
    "Antrectomia com vagotomia e reconstrução Billroth I / II",
    "Abordagem laparoscópica (vagotomia / antrectomia)",
  ],
  "Tumor Benigno Gástrico (GIST / Leiomioma)": [
    "Gastrectomia parcial laparoscópica com ressecção em cunha",
    "Gastrectomia parcial aberta com ressecção em cunha",
    "Ressecção intragástrica laparoscópica (lesões submucosas intraluminais)",
  ],
  "Estenose Pilórica do Adulto": [
    "Piloroplastia laparoscópica (Heineke-Mikulicz)",
    "Gastrectomia parcial distal laparoscópica com reconstrução",
    "Gastrectomia parcial distal aberta",
  ],
  "Aderências / Bridas Intestinais (cirurgia eletiva)": [
    "Lise de aderências intestinais por videolaparoscopia",
    "Lise de aderências intestinais por laparotomia (relaparotomia)",
  ],
  "Tumor Benigno de Intestino Delgado": [
    "Ressecção segmentar de intestino delgado com anastomose primária — laparoscópica",
    "Ressecção segmentar de intestino delgado com anastomose primária — aberta",
  ],
  "Doença de Crohn — Ressecção Eletiva": [
    "Ressecção ileocecal laparoscópica com anastomose primária",
    "Ressecção ileocecal aberta com anastomose primária",
    "Ressecção segmentar de intestino delgado laparoscópica",
    "Estricturoplastia (estenose sem massa palpável)",
  ],
  "Divertículo de Meckel Sintomático": [
    "Diverticulectomia de Meckel laparoscópica",
    "Diverticulectomia de Meckel aberta",
    "Ressecção segmentar ileal laparoscópica (base larga / suspeita de malignidade)",
  ],
  "Fístula Enterocutânea": [
    "Ressecção do segmento intestinal fistulizado com anastomose primária",
    "Ressecção com anastomose primária + colostomia de proteção",
  ],
  "Doença Diverticular do Cólon Sintomática": [
    "Sigmoidectomia laparoscópica com anastomose primária colorretal",
    "Sigmoidectomia robótica com anastomose primária",
    "Sigmoidectomia aberta com anastomose primária",
    "Operação de Hartmann laparoscópica (sigmoidectomia + colostomia terminal)",
  ],
  "Pólipo Colônico de Grande Volume (não ressecável por colonoscopia)": [
    "Ressecção colônica segmentar laparoscópica",
    "Hemicolectomia direita / esquerda laparoscópica conforme localização",
    "Ressecção colônica segmentar aberta",
  ],
  "Megacólon Chagásico": [
    "Retossigmoidectomia com abaixamento coloanal — técnica de Duhamel-Haddad",
    "Retossigmoidectomia com abaixamento coloanal — técnica de Swenson",
    "Coloproctectomia total com anastomose íleo-retal (casos extensos)",
  ],
  "Constipação Crônica de Causa Colônica": [
    "Colectomia total com anastomose íleo-retal laparoscópica",
    "Colectomia subtotal com anastomose íleo-sigmoide laparoscópica",
  ],
  "Colite Ulcerativa — Cirurgia Eletiva": [
    "Proctocolectomia total com reservatório ileal (bolsa em J — IPAA) laparoscópica",
    "Proctocolectomia total com ileostomia terminal definitiva laparoscópica",
    "Colectomia total com ileostomia + segundo tempo (mucosectomia + IPAA)",
  ],
  "Doença de Crohn Colônica — Cirurgia Eletiva": [
    "Hemicolectomia direita laparoscópica",
    "Hemicolectomia esquerda laparoscópica",
    "Colectomia segmentar laparoscópica",
    "Colectomia total laparoscópica",
  ],
  "Prolapso Retal": [
    "Retopexia laparoscópica anterior com tela (técnica de d'Hoore / ventral mesh rectopexy)",
    "Retopexia laparoscópica posterior (técnica de Wells)",
    "Retopexia robótica anterior com tela",
    "Retossigmoidectomia perineal (técnica de Altemeier) — acesso perineal",
    "Operação de Delorme — acesso perineal",
  ],
  "Retocele Sintomática": [
    "Correção de retocele por via transanal",
    "Correção de retocele por via transvaginal (colporrafia posterior)",
    "Correção de retocele laparoscópica com tela (retopexia ventral)",
  ],
  "Estenose Retal Benigna": [
    "Dilatação endoanal progressiva da estenose retal",
    "Ressecção endoanal da estenose + plastia (avanço de retalho)",
    "Ressecção transanal endoscópica microcirúrgica (TEM / TAMIS)",
  ],
  "Hemorróidas Grau III / IV": [
    "Hemorroidectomia aberta — técnica de Milligan-Morgan",
    "Hemorroidectomia fechada — técnica de Ferguson",
    "Hemorroidopexia com grampeador circular — PPH (procedimento de Longo)",
    "HAL-RAR (ligadura das artérias hemorroidárias com rafia do prolápso — Doppler-guiada)",
    "Hemorroidectomia com bisturi harmônico / Ligasure",
  ],
  "Fissura Anal Crônica": [
    "Esfincterotomia interna lateral fechada",
    "Esfincterotomia interna lateral aberta",
    "Avanço de retalho cutâneo (casos sem reserva esfinctérica)",
  ],
  "Fístula Perianal (transesfincteriana / supraesfincteriana)": [
    "Colocação de Seton de corte progressivo",
    "Colocação de Seton dreno (sem corte) + segundo tempo",
    "LIFT — ligadura interesfincteriana do trato fistuloso",
    "Avanço de retalho endorretal (endorectal flap advancement)",
    "Plug de fístula (fistula plug bioprotético)",
    "Laser de fístula (FiLaC — fistula-tract laser closure)",
    "VAAFT — cirurgia assistida por vídeo para fístula anorretal",
  ],
  "Fístula Perianal Baixa (interesfincteriana / submucosa)": [
    "Fistulotomia com abertura completa do trato fistuloso",
    "Fistulectomia com excisão do trato e sutura primária",
  ],
  "Abscesso Anorretal Recorrente": [
    "Drenagem cirúrgica de abscesso anorretal com pesquisa e tratamento de fístula associada",
    "Drenagem cirúrgica simples de abscesso anorretal",
  ],
  "Cisto Pilonidal / Seio Pilonidal": [
    "Exérese de cisto pilonidal com fechamento primário — técnica de Karydakis",
    "Exérese de cisto pilonidal com retalho romboide — técnica de Limberg",
    "Exérese de cisto pilonidal com cicatrização por segunda intenção",
    "Exérese de cisto pilonidal com sutura primária em linha média",
    "Sinusectomia de Bascom (curetagem dos óstios)",
  ],
  "Condiloma Acuminado Perianal (extenso)": [
    "Exérese cirúrgica de condiloma acuminado perianal",
    "Eletrocauterização / coagulação de condiloma perianal",
    "Laser CO₂ de condiloma acuminado perianal",
  ],
  "Incontinência Fecal — Esfincteroplastia Eletiva": [
    "Esfincteroplastia anal anterior sobreposta (sobreposição muscular)",
    "Neuromodulação sacral (implante de eletrodo sacral — SNM)",
    "Esfincteroplastia + graciloplastia dinâmica (casos selecionados)",
  ],
  "Hidradenite Supurativa Perianal": [
    "Exérese ampla de hidradenite supurativa perianal + enxertia de pele",
    "Exérese ampla + cicatrização por segunda intenção",
    "Exérese ampla + retalho cutâneo local",
  ],
  "Cisto Hepático Simples Sintomático": [
    "Deroofing laparoscópico de cisto hepático simples",
    "Deroofing aberto de cisto hepático simples",
    "Drenagem percutânea com escleroterapia (PAIR — percutaneous aspiration, injection, reaspiration)",
  ],
  "Cisto Hidático Hepático": [
    "Cistopericistecomia hepática laparoscópica",
    "Cistopericistecomia hepática aberta",
    "Drenagem percutânea com escleroterapia (PAIR) — pré-operatório ou definitiva",
  ],
  "Hepatolitíase": [
    "Colangioscopia percutânea trans-hepática com litotripsia",
    "Ressecção hepática segmentar laparoscópica",
    "Ressecção hepática segmentar aberta",
  ],
  "Hemangioma Hepático Sintomático": [
    "Ressecção hepática laparoscópica (hepatectomia segmentar / enucleação)",
    "Ressecção hepática aberta (hepatectomia segmentar / enucleação)",
  ],
  "Adenoma Hepático": [
    "Ressecção hepática laparoscópica",
    "Ressecção hepática aberta",
    "Embolização arterial transcateter + ressecção diferida (casos selecionados)",
  ],
  "Hipertensão Portal — Shunt Cirúrgico Eletivo": [
    "Shunt esplenorrenal distal de Warren (anastomose esplenorrenal distal)",
    "Shunt meso-cava com interposição de prótese",
    "Shunt porto-cava laterolateral",
    "TIPS (shunt portossistêmico trans-hepático intrajugular) — procedimento radiológico",
  ],
  "Pancreatite Crônica — Cirurgia Eletiva (Frey / Puestow / Beger)": [
    "Procedimento de Frey (ressecção-drenagem da cabeça + pancreatojejunostomia longitudinal)",
    "Procedimento de Puestow-Gillesby (pancreatojejunostomia longitudinal laterolateral em Y de Roux)",
    "Procedimento de Beger (duodenopancreatectomia parcial com preservação do duodeno)",
    "Pancreatectomia distal laparoscópica",
  ],
  "Pseudocisto Pancreático Sintomático": [
    "Cistojejunoanastomose laparoscópica em Y de Roux",
    "Cistogastroanastomose laparoscópica",
    "Cistojejunoanastomose aberta em Y de Roux",
    "Drenagem percutânea guiada por imagem (casos selecionados)",
    "Drenagem endoscópica trans-mural (ecoendoscopia)",
  ],
  "Cistoadenoma Seroso / Mucinoso do Pâncreas": [
    "Pancreatectomia distal laparoscópica com preservação esplênica (técnica de Warshaw / Kimura)",
    "Pancreatectomia distal laparoscópica com esplenectomia",
    "Pancreatectomia distal robótica",
    "Pancreatectomia distal aberta",
    "Enucleação laparoscópica (lesões pequenas e periféricas)",
  ],
  "Esplenomegalia — Esplenectomia Eletiva": [
    "Esplenectomia videolaparoscópica eletiva",
    "Esplenectomia robótica",
    "Esplenectomia aberta (esplenomegalia volumosa > 20 cm)",
    "Esplenectomia laparoscópica com preservação de esplenúnculos",
  ],
  "Cisto Esplênico Sintomático": [
    "Esplenectomia laparoscópica",
    "Marsupialização laparoscópica de cisto esplênico (preservação do baço)",
    "Ressecção parcial esplênica laparoscópica",
  ],
  "Bócio Nodular — Tireoidectomia Parcial / Total": [
    "Tireoidectomia total (acesso cervical convencional)",
    "Tireoidectomia total robótica (acesso axilar / BABA)",
    "Lobectomia tireoidiana com istmectomia (hemitireoidectomia)",
    "Tireoidectomia total videoassistida (MIVAT — minimally invasive video-assisted)",
  ],
  "Nódulo de Tireoide Indeterminado (Bethesda III / IV)": [
    "Lobectomia tireoidiana com istmectomia (hemitireoidectomia)",
    "Tireoidectomia total (se fatores de risco elevados ou bilateral)",
    "Lobectomia robótica (acesso axilar)",
  ],
  "Hipertireoidismo Refratário ao Tratamento Clínico": [
    "Tireoidectomia total (acesso cervical convencional)",
    "Tireoidectomia total videoassistida (MIVAT)",
    "Tireoidectomia total robótica",
  ],
  "Hiperparatireoidismo Primário — Paratireoidectomia": [
    "Paratireoidectomia guiada por PTH intraoperatório + cintilografia MIBI (cirurgia minimamente invasiva)",
    "Paratireoidectomia bilateral com exploração das quatro glândulas",
    "Paratireoidectomia radioguiada (scintigrafia + sonda gama intraoperatória)",
  ],
  "Adenoma de Paratireoide": [
    "Paratireoidectomia seletiva guiada por PTH intraoperatório",
    "Paratireoidectomia radioguiada",
    "Paratireoidectomia bilateral com exploração completa",
  ],
  "Empiema Pleural Crônico (decorticação eletiva)": [
    "Decorticação pleural por videotoracoscopia (VATS)",
    "Decorticação pleural por toracotomia aberta",
  ],
  "Cisto Mediastinal Benigno": [
    "Exérese de cisto mediastinal por videotoracoscopia (VATS)",
    "Exérese de cisto mediastinal robótica",
    "Exérese de cisto mediastinal por esternotomia / toracotomia",
  ],
  "Tumor de Parede Torácica Benigno": [
    "Ressecção de tumor de parede torácica (com ou sem ressecção costal)",
    "Ressecção por VATS (lesões selecionadas)",
  ],
  "Fibroadenoma de Mama": [
    "Tumorectomia de mama (exérese de fibroadenoma com margem de segurança)",
    "Exérese guiada por ultrassom intraoperatório",
  ],
  "Tumor Filodes Benigno de Mama": [
    "Exérese ampla de tumor filodes com margem de 1–2 cm",
    "Mastectomia simples (tumores volumosos / recorrentes)",
  ],
  "Ginecomastia": [
    "Mastectomia subcutânea bilateral (lipoaspiração + exérese glandular)",
    "Mastectomia subcutânea bilateral aberta (sem lipoaspiração)",
  ],
  "Abscesso Mamário Recorrente / Fístula de Ducto": [
    "Microdochectomia (exérese do ducto fistuloso)",
    "Exérese de fístula mamária periareolar",
    "Ducto-extirpação central (exérese de complexo areolo-papilar e ductos centrais)",
  ],
  "Cisto Mamário Volumoso / Recorrente": [
    "Exérese cirúrgica de cisto mamário",
    "Punção aspirativa guiada por ultrassom + análise do líquido",
  ],
  "Cisto Sebáceo / Epidérmico": [
    "Exérese de cisto sebáceo / epidérmico em consultório ou centro cirúrgico",
    "Exérese com cápsula íntegra (técnica de punch — incisão mínima)",
  ],
  "Lipoma": [
    "Exérese de lipoma — ressecção cirúrgica convencional",
    "Exérese de lipoma — lipoaspiração (lipomas superficiais)",
  ],
  "Fibroma / Dermatofibroma": [
    "Exérese de fibroma / dermatofibroma com margem mínima",
  ],
  "Nevo Melanocítico — Exérese Eletiva": [
    "Exérese de nevo melanocítico com margens de 2–5 mm (nevos benignos)",
    "Exérese de nevo melanocítico com margens ampliadas (displasia / Breslow > 1 mm)",
  ],
  "Queratose Seborreica Complicada": [
    "Exérese cirúrgica de queratose seborreica",
    "Eletrocauterização / criocirurgia de queratose seborreica",
  ],
  "Granuloma Piogênico": [
    "Exérese cirúrgica de granuloma piogênico",
    "Cauterização / eletrocirurgia de granuloma piogênico",
    "Laser de granuloma piogênico",
  ],
  "Carcinoma Basocelular / Espinocelular (ressecção eletiva)": [
    "Ressecção de carcinoma cutâneo com margens oncológicas (1 cm para CEB / 4–6 mm para CBC)",
    "Cirurgia de Mohs (carcinoma de alto risco em área de risco / recorrente)",
    "Ressecção + reconstrução com retalho local",
    "Ressecção + enxertia de pele",
  ],
  "Cirurgia Ambulatorial Dermatológica Geral": [
    "Exérese de lesão cutânea / subcutânea",
    "Exérese de lesão cutânea com sutura primária",
    "Exérese de lesão cutânea com retalho local",
  ],
};

const ANAMNESE_POR_MOTIVO = {
  // ── HÉRNIAS INGUINAIS ──────────────────────────────────────────────────────
  "Hérnia Inguinal Direita":
    "Paciente refere aumento de volume em região inguinal direita há [X] meses/anos, com dor e desconforto local que se intensificam aos esforços físicos, tosse, espirros e posição ortostática prolongada. Abaulamento de redução espontânea ao deitar. Nega episódios de encarceramento ou estrangulamento. Sem febre, alterações do hábito intestinal ou sintomas urinários. Solicita avaliação cirúrgica para tratamento definitivo.",
  "Hérnia Inguinal Esquerda":
    "Paciente refere aumento de volume em região inguinal esquerda há [X] meses/anos, com dor e desconforto local que se intensificam aos esforços físicos, tosse, espirros e posição ortostática prolongada. Abaulamento de redução espontânea ao deitar. Nega episódios de encarceramento ou estrangulamento. Sem febre, alterações do hábito intestinal ou sintomas urinários. Solicita avaliação cirúrgica para tratamento definitivo.",
  "Hérnia Inguinal Bilateral":
    "Paciente refere aumento de volume em ambas as regiões inguinais há [X] meses/anos, com dor e desconforto local bilateral que se intensificam aos esforços, tosse e posição ortostática. Nega encarceramento prévio. Sem febre ou alterações do trânsito intestinal. Solicita avaliação cirúrgica.",
  "Hérnia Inguinal Direita Recidivada":
    "Paciente refere recidiva de hérnia inguinal direita após cirurgia prévia realizada em [data/local]. Relata retorno do abaulamento há [X] meses, com desconforto e dor local progressivos. Nega encarceramento. Traz documentação da cirurgia anterior.",
  "Hérnia Inguinal Esquerda Recidivada":
    "Paciente refere recidiva de hérnia inguinal esquerda após cirurgia prévia realizada em [data/local]. Relata retorno do abaulamento há [X] meses, com desconforto e dor local progressivos. Nega encarceramento. Traz documentação da cirurgia anterior.",
  "Hérnia Inguinal Bilateral Recidivada":
    "Paciente refere recidiva de hérnia inguinal bilateral após cirurgia prévia realizada em [data/local]. Relata retorno de abaulamento bilateral há [X] meses com desconforto progressivo. Nega encarceramento.",
  // ── HÉRNIAS CRURAIS ───────────────────────────────────────────────────────
  "Hérnia Crural Direita":
    "Paciente refere abaulamento em região crural direita há [X] meses, com dor local e sensação de peso. Piora com esforços e posição ortostática. Redutível ao decúbito. Nega encarceramento.",
  "Hérnia Crural Esquerda":
    "Paciente refere abaulamento em região crural esquerda há [X] meses, com dor local e sensação de peso. Piora com esforços e posição ortostática. Redutível ao decúbito. Nega encarceramento.",
  "Hérnia Crural Bilateral":
    "Paciente refere abaulamento em ambas as regiões crurais há [X] meses, com dor e desconforto bilateral, piora com esforços. Redutível ao decúbito. Nega encarceramento.",
  // ── HÉRNIAS DA PAREDE ────────────────────────────────────────────────────
  "Hérnia Umbilical":
    "Paciente refere aumento de volume em região umbilical há [X] meses/anos, com desconforto e dor local que pioram aos esforços. Abaulamento de redução espontânea ao decúbito. Nega encarceramento prévio. Solicita avaliação para correção cirúrgica eletiva.",
  "Hérnia Umbilical Recidivada":
    "Paciente refere recidiva de hérnia umbilical após correção cirúrgica prévia realizada em [data]. Relata retorno do abaulamento umbilical há [X] meses com dor aos esforços. Nega encarceramento.",
  "Hérnia Epigástrica":
    "Paciente refere abaulamento em região epigástrica (linha alba) há [X] meses, com dor local intermitente, piora pós-prandial e aos esforços. Redutível ao decúbito. Nega encarceramento.",
  "Hérnia Incisional":
    "Paciente refere abaulamento em cicatriz cirúrgica abdominal prévia ([descrever cirurgia/data]) há [X] meses, com dor e sensação de peso progressivos. Aumento do volume ao esforço. Nega encarceramento. Impacto na qualidade de vida e limitação de atividades.",
  "Hérnia Incisional Recidivada":
    "Paciente refere nova recidiva de hérnia incisional após múltiplas correções prévias. Abaulamento em região de cicatriz anterior com dor e limitação funcional. Nega encarceramento no momento.",
  "Hérnia de Spiegel":
    "Paciente refere dor abdominal em flanco [D/E], sem abaulamento visível evidente, porém com massa palpável ao esforço na região de linha semilunar. Sintomas há [X] meses. Diagnóstico confirmado por ultrassonografia/TC de abdômen.",
  "Hérnia Lombar":
    "Paciente refere abaulamento em região lombar [D/E] há [X] meses, com dor local e lombalgia associada. Piora com esforços e posição ortostática. Diagnóstico confirmado por imagem.",
  "Hérnia Obturadora":
    "Paciente refere dor em face interna da coxa [D/E], com irradiação para joelho (sinal de Howship-Romberg). Diagnóstico confirmado por TC de pelve. Encaminhada para correção cirúrgica.",
  "Hérnia Paraesofágica / Hiatal":
    "Paciente refere pirose, regurgitação e dor retroesternal há [X] meses/anos, com piora ao deitar e após refeições. Episódios de vômitos ocasionais. Diagnóstico de hérnia hiatal confirmado por endoscopia digestiva alta e/ou esofagograma. Sem resposta satisfatória ao tratamento clínico prolongado. Encaminhado para avaliação de correção cirúrgica.",
  "Diástase dos Retos Abdominais":
    "Paciente refere abaulamento abdominal central, principalmente ao esforço e à contração muscular, com sensação de fraqueza abdominal e dor lombar associada. Histórico de [gestação(ões)/cirurgias abdominais]. Diagnóstico de diástase dos retos confirmado por exame físico e ultrassonografia de parede abdominal.",
  // ── VESÍCULA E VIAS BILIARES ─────────────────────────────────────────────
  "Colelitíase / Colecistite Crônica Calculosa":
    "Paciente refere episódios recorrentes de dor em hipocôndrio direito e/ou epigástrio, de caráter cólico, com irradiação para dorso e escápula direita, associados à ingestão de alimentos gordurosos. Náuseas e vômitos durante as crises. Diagnóstico de colelitíase confirmado por ultrassonografia abdominal ([X] cálculos, maior medindo [X] mm). Sem icterícia, acolia fecal ou colúria. Nega febre. Indica-se colecistectomia eletiva.",
  "Colecistite Aguda (eletiva após resolução)":
    "Paciente com histórico de colecistite aguda tratada conservadoramente em [data], com resolução do quadro inflamatório. Ultrassonografia de controle confirma colelitíase. Encaminhado para colecistectomia eletiva no intervalo de 6–8 semanas.",
  "Coledocolitíase":
    "Paciente refere episódios de icterícia obstrutiva, dor em hipocôndrio direito e colúria. Diagnóstico de coledocolitíase confirmado por ultrassonografia/colangioRNM (coledocolitíase com dilatação de vias biliares). Aguarda CPRE para extração do cálculo e colecistectomia laparoscópica em seguida.",
  "Pólipo de Vesícula Biliar":
    "Paciente assintomático ou com queixa de desconforto em hipocôndrio direito. Diagnóstico de pólipo de vesícula biliar ao ultrassom (medindo [X] mm). Indicação de colecistectomia por pólipo ≥ 10 mm e/ou crescimento progressivo em exames seriados.",
  "Colangite Crônica":
    "Paciente refere episódios recorrentes de febre, icterícia e dor em hipocôndrio direito (tríade de Charcot). Exames de imagem evidenciam colelitíase e espessamento da parede das vias biliares. Indicada colecistectomia com exploração das vias biliares.",
  // ── ESÔFAGO E ESTÔMAGO ───────────────────────────────────────────────────
  "Doença do Refluxo Gastroesofágico (DRGE) — Fundoplicatura":
    "Paciente refere pirose e regurgitação ácida há [X] anos, com piora ao deitar-se, após refeições volumosas e com ingestão de bebidas alcoólicas/café. Relata disfagia ocasional e tosse crônica. Endoscopia digestiva alta evidencia esofagite grau [A–D de Los Angeles]. pH-metria de 24h confirma DRGE. Sem resposta adequada ao tratamento clínico com IBP em dose plena por > 6 meses. Indicado tratamento cirúrgico.",
  "Acalasia de Esôfago":
    "Paciente refere disfagia progressiva para sólidos e líquidos há [X] meses/anos, com regurgitação de alimentos não digeridos, dor retroesternal e perda de peso. Diagnóstico confirmado por manometria esofágica de alta resolução (pressão do EEI elevada, aperistalse). Esofagograma com sinal do 'bico de pássaro'. Indicado tratamento cirúrgico ou endoscópico.",
  "Divertículo de Zenker":
    "Paciente refere disfagia progressiva, regurgitação de alimentos não digeridos, halitose e episódios de engasgos. Diagnóstico de divertículo de Zenker confirmado por esofagograma baritado. Indica-se tratamento cirúrgico ou endoscópico.",
  "Úlcera Péptica Gástrica Refratária":
    "Paciente refere epigastralgia em queimação há [X] anos, sem resposta adequada ao tratamento clínico com IBP e erradicação de H. pylori. Endoscopia digestiva alta confirma úlcera péptica gástrica refratária. Biópsia sem malignidade. Indicado tratamento cirúrgico.",
  "Úlcera Péptica Duodenal Refratária":
    "Paciente refere epigastralgia em queimação com melhora com a alimentação há [X] anos. Refratário ao tratamento clínico e erradicação de H. pylori. Endoscopia confirma úlcera duodenal refratária. Indicado tratamento cirúrgico.",
  // ── CÓLON E RETO ─────────────────────────────────────────────────────────
  "Doença Diverticular do Cólon Sintomática":
    "Paciente refere episódios recorrentes de dor em fossa ilíaca esquerda, febre, alterações do hábito intestinal e flatulência. Diagnóstico de doença diverticular do sigmoide confirmado por colonoscopia e/ou TC de abdômen (Hinchey I/II tratados conservadoramente). Indica-se sigmoidectomia eletiva após [X] episódios de diverticulite.",
  "Megacólon Chagásico":
    "Paciente refere constipação intestinal crônica grave há [X] anos, com períodos de obstipação prolongada (> 7–10 dias), distensão abdominal e necessidade de laxantes/enemas frequentes. Diagnóstico de megacólon chagásico confirmado por enema opaco e sorologia para Chagas positiva. Indicado tratamento cirúrgico.",
  "Colite Ulcerativa — Cirurgia Eletiva":
    "Paciente portador de retocolite ulcerativa há [X] anos, com múltiplos surtos, refratário ao tratamento clínico otimizado (corticoide, mesalazina, imunossupressores, biológicos). Colonoscopia com displasia de alto grau / pancolite refratária. Indicada proctocolectomia total eletiva.",
  // ── ANORRETAL ────────────────────────────────────────────────────────────
  "Hemorróidas Grau III / IV":
    "Paciente refere prolapso hemorroidário recorrente, sangramento retal vivo ao esforço defecatório, dor, prurido e desconforto perianal há [X] meses/anos. Grau III (redução manual necessária) / IV (irredutível). Colonoscopia descartou outras causas de sangramento. Sem resposta satisfatória ao tratamento conservador. Indicado tratamento cirúrgico.",
  "Fissura Anal Crônica":
    "Paciente refere dor anal intensa e aguda durante e após a evacuação há [X] meses, associada a sangramento retal vivo escasso e espasmo do esfíncter anal. Diagnóstico de fissura anal crônica confirmado ao exame proctológico (presença de fibra de esfíncter interno). Sem resposta ao tratamento clínico (nitratos, bloqueadores de canal de cálcio tópicos). Indica-se esfincterotomia interna lateral.",
  "Fístula Perianal (transesfincteriana / supraesfincteriana)":
    "Paciente refere secreção purulenta crônica em região perianal há [X] meses, com abscesso perianal drenado espontaneamente ou cirurgicamente em [data]. Exame proctológico confirma orifício externo de fístula a [X] cm da borda anal. RM de pelve confirma trajeto fistuloso transesfincteriano. Indicado tratamento cirúrgico.",
  "Fístula Perianal Baixa (interesfincteriana / submucosa)":
    "Paciente refere secreção perianal crônica há [X] meses, com antecedente de abscesso perianal. Exame proctológico confirma fístula perianal baixa (interesfincteriana / submucosa). Indica-se fistulotomia eletiva.",
  "Cisto Pilonidal / Seio Pilonidal":
    "Paciente refere dor, secreção purulenta e abaulamento em região sacrococcígea há [X] meses, com episódios recorrentes de infecção. Diagnóstico de cisto/seio pilonidal confirmado ao exame físico. Nega episódios febreis no momento. Indica-se exérese eletiva.",
  "Hemorróidas Grau III / IV":
    "Paciente refere sangramento retal e prolapso hemorroidário frequentes há [X] meses. Classifica-se como grau III/IV ao exame proctológico. Indica-se tratamento cirúrgico eletivo.",
  // ── TIREOIDE ─────────────────────────────────────────────────────────────
  "Bócio Nodular — Tireoidectomia Parcial / Total":
    "Paciente refere aumento de volume cervical anterior progressivo há [X] meses/anos, com sensação de desconforto cervical, disfagia e/ou disfonia ocasionais. Ultrassonografia tireoidiana evidencia bócio multinodular ([descrever nódulos]). TSH e T4 livre [normais / alterados]. PAAF: Bethesda [II/III/IV]. Indicada tireoidectomia.",
  "Nódulo de Tireoide Indeterminado (Bethesda III / IV)":
    "Paciente com nódulo tireoidiano incidental / palpável, sem sintomas compressivos. Ultrassonografia evidencia nódulo em lobo [D/E], medindo [X] mm, com características [descrição]. PAAF: resultado Bethesda [III/IV] — indeterminado/suspeito de neoplasia folicular. TSH normal. Indica-se lobectomia diagnóstico-terapêutica.",
  "Hipertireoidismo Refratário ao Tratamento Clínico":
    "Paciente refere perda de peso, tremores, palpitações, intolerância ao calor e nervosismo há [X] meses. Diagnóstico de hipertireoidismo confirmado por TSH suprimido e T4 livre elevado. Cintilografia tireoidiana: [achado]. Sem resposta adequada ao tratamento com tionamidas e/ou radioiodo. Indica-se tireoidectomia total.",
  "Hiperparatireoidismo Primário — Paratireoidectomia":
    "Paciente com diagnóstico de hiperparatireoidismo primário confirmado por hipercalcemia persistente e PTH elevado. Cintilografia de paratireoides (MIBI) e/ou ultrassonografia cervical evidenciam adenoma em glândula [descrever]. Sintomas: [nefrolitíase / osteoporose / fadiga / hipercalciúria]. Indica-se paratireoidectomia.",
  // ── MAMA ─────────────────────────────────────────────────────────────────
  "Fibroadenoma de Mama":
    "Paciente refere nódulo palpável em mama [D/E] há [X] meses, sem dor, secreção papilar ou alterações cutâneas. Ultrassonografia mamária confirma nódulo sólido, bem delimitado, com características compatíveis com fibroadenoma (BI-RADS [3/4A]), medindo [X] mm. Core biopsy / PAAF: fibroadenoma. Indica-se exérese eletiva.",
  "Ginecomastia":
    "Paciente refere aumento bilateral/unilateral do tecido glandular mamário há [X] meses/anos, com desconforto local e impacto psicossocial. Sem uso de medicamentos causadores de ginecomastia secundária. Exames hormonais sem alterações significativas. Indica-se tratamento cirúrgico.",
  // ── PARTES MOLES / DERMATOLOGIA ──────────────────────────────────────────
  "Cisto Sebáceo / Epidérmico":
    "Paciente refere nódulo subcutâneo em [localização] há [X] meses, indolor, de crescimento lento, com orifício central visível. Episódio de inflamação/infecção prévia em [data]. Nega secreção ativa no momento. Solicita exérese cirúrgica.",
  "Lipoma":
    "Paciente refere nódulo subcutâneo em [localização] há [X] meses/anos, de consistência amolecida, indolor, móvel e bem delimitado. Crescimento lento e progressivo. Solicita exérese para alívio sintomático e confirmação diagnóstica.",
  "Carcinoma Basocelular / Espinocelular (ressecção eletiva)":
    "Paciente refere lesão cutânea em [localização] há [X] meses, com crescimento progressivo, sangramento ocasional e não cicatrização. Biópsia prévia confirma carcinoma [basocelular / espinocelular]. Sem evidências de metástase. Indica-se ressecção com margens oncológicas.",
  "Nevo Melanocítico — Exérese Eletiva":
    "Paciente refere lesão pigmentada em [localização] com alterações recentes (critério ABCDE: [descrever]). Solicita exérese para análise histopatológica e tratamento definitivo.",
};

const getAnamnese = (motivo, procedimento) => {
  if (ANAMNESE_POR_MOTIVO[motivo]) return ANAMNESE_POR_MOTIVO[motivo];
  const proc = procedimento && procedimento !== "__custom__" ? procedimento : "procedimento a definir";
  return `Paciente encaminhado para avaliação cirúrgica eletiva com diagnóstico de ${motivo}. Relata sintomas compatíveis com a patologia de base há [X] meses/anos, com repercussão na qualidade de vida e limitação de atividades cotidianas. Exames complementares confirmam o diagnóstico. Sem episódios agudos recentes. Indica-se tratamento cirúrgico eletivo: ${proc}.`;
};

const EXAME_FISICO_POR_MOTIVO = {
  // ── HÉRNIAS INGUINAIS ────────────────────────────────────────────────────
  "Hérnia Inguinal Direita":
    "Bom estado geral, corado, hidratado, afebril. PA: [X] mmHg. FC: [X] bpm. Peso: [X] kg. Abdômen plano, flácido, sem visceromegalias. À inspeção e palpação da região inguinal direita: abaulamento visível / palpável à manobra de Valsalva, de conteúdo redutível, sem sinais de encarceramento ou estrangulamento (nega dor intensa, sem febre, sem sinais de irritação peritoneal). Anel inguinal externo [alargado]. Anel inguinal interno digitalmente patente.",
  "Hérnia Inguinal Esquerda":
    "Bom estado geral, corado, hidratado, afebril. Abdômen plano, flácido. À palpação da região inguinal esquerda: abaulamento palpável à manobra de Valsalva, redutível, sem sinais de encarceramento. Anel inguinal externo alargado à esquerda.",
  "Hérnia Inguinal Bilateral":
    "Bom estado geral, corado, hidratado, afebril. Abdômen plano, flácido. Abaulamento bilateral nas regiões inguinais à manobra de Valsalva, ambos redutíveis, sem sinais de encarceramento ou estrangulamento. Anéis inguinais externos alargados bilateralmente.",
  "Hérnia Inguinal Direita Recidivada":
    "Bom estado geral. Cicatriz cirúrgica em região inguinal direita (herniorrafia prévia). Abaulamento recidivado palpável à manobra de Valsalva, redutível. Sem sinais flogísticos sobre a cicatriz. Anel inguinal patente.",
  "Hérnia Inguinal Esquerda Recidivada":
    "Bom estado geral. Cicatriz cirúrgica em região inguinal esquerda (herniorrafia prévia). Abaulamento recidivado palpável à Valsalva, redutível. Sem sinais flogísticos.",
  "Hérnia Inguinal Bilateral Recidivada":
    "Bom estado geral. Cicatrizes de herniorrafias prévias bilaterais. Abaulamentos recidivados bilaterais à Valsalva, redutíveis. Sem sinais flogísticos.",
  // ── HÉRNIAS CRURAIS ──────────────────────────────────────────────────────
  "Hérnia Crural Direita":
    "Bom estado geral. Abaulamento palpável na região crural/femoral direita (medial ao ligamento inguinal), de pequenas dimensões, redutível à palpação. Sem sinais de encarceramento. Anel femoral palpável.",
  "Hérnia Crural Esquerda":
    "Bom estado geral. Abaulamento palpável na região crural/femoral esquerda, redutível. Sem sinais de encarceramento.",
  "Hérnia Crural Bilateral":
    "Bom estado geral. Abaulamentos palpáveis em ambas as regiões femorais, redutíveis. Sem sinais de encarceramento bilateral.",
  // ── HÉRNIAS DA PAREDE ───────────────────────────────────────────────────
  "Hérnia Umbilical":
    "Bom estado geral, corado, hidratado. Abdômen globoso / plano. À inspeção: abaulamento umbilical visível em ortostatismo. À palpação: defeito da parede aponeurótica umbilical (diâmetro aproximado: [X] cm), conteúdo redutível ao decúbito, sem sinais de encarceramento. Anel umbilical alargado.",
  "Hérnia Umbilical Recidivada":
    "Bom estado geral. Cicatriz umbilical de herniorrafia prévia. Novo defeito herniário umbilical palpável, redutível. Sem sinais flogísticos ou encarceramento.",
  "Hérnia Epigástrica":
    "Bom estado geral. À palpação da linha alba em região epigástrica: nódulo / defeito aponeurótico de [X] cm, conteúdo lipomatoso / redutível. Sem sinais de encarceramento. Dor leve à digitopressão.",
  "Hérnia Incisional":
    "Bom estado geral. Cicatriz cirúrgica abdominal ([descrever localização]) com abaulamento ao longo da incisão. Defeito da parede aponeurótica de aproximadamente [X] × [X] cm à palpação. Conteúdo redutível ao decúbito. Sem sinais de encarceramento. Pele da cicatriz íntegra / com alterações tróficas.",
  "Hérnia Incisional Recidivada":
    "Bom estado geral. Cicatrizes de correções prévias. Defeito herniário recidivado de [X] cm, conteúdo redutível. Sem encarceramento.",
  "Hérnia de Spiegel":
    "Abdômen sem abaulamento visível. À palpação bimanual da região de linha semilunar [D/E], detecta-se massa palpável ao esforço / manobra de Valsalva, de difícil delimitação ao repouso. Sem sinais de encarceramento.",
  "Hérnia Lombar":
    "Abaulamento visível/palpável em região lombar [D/E]. Conteúdo redutível, sem dor intensa. Defeito aponeurótico palpável.",
  "Hérnia Obturadora":
    "Bom estado geral. Sinal de Howship-Romberg positivo (dor na face interna da coxa à rotação interna). Massa de difícil palpação em região obturadora.",
  "Hérnia Paraesofágica / Hiatal":
    "Bom estado geral. Abdômen sem abaulamento. Sem dor à palpação epigástrica no momento. Sem sinais de complicações agudas.",
  "Diástase dos Retos Abdominais":
    "Abdômen com abaulamento central na linha alba, evidenciado à elevação ativa do tronco (head-lift test positivo). Diástase dos retos abdominais palpável, de aproximadamente [X] cm de largura. Sem defeito herniário associado.",
  // ── VESÍCULA ────────────────────────────────────────────────────────────
  "Colelitíase / Colecistite Crônica Calculosa":
    "Bom estado geral, corado, hidratado, afebril. Ictérico: não. Abdômen plano, flácido, ruídos hidroaéreos presentes. Leve dor à palpação profunda em hipocôndrio direito / ponto cístico. Sinal de Murphy: negativo no momento. Vesícula biliar não palpável. Sem sinais de peritonismo.",
  "Colecistite Aguda (eletiva após resolução)":
    "Bom estado geral, afebril. Abdômen com leve sensibilidade em hipocôndrio direito à palpação profunda. Sinal de Murphy negativo no momento. Sem icterícia. Quadro inflamatório agudo resolvido.",
  "Coledocolitíase":
    "Bom estado geral. Icterícia discreta/moderada em escleras e pele. Colúria referida. Abdômen com dor à palpação em hipocôndrio direito e epigástrio. Sinal de Murphy: [positivo/negativo]. Sem sinais de peritonismo.",
  "Pólipo de Vesícula Biliar":
    "Bom estado geral, corado, hidratado, afebril. Abdômen sem dor à palpação. Vesícula biliar não palpável. Exame físico sem alterações significativas.",
  "Colangite Crônica":
    "Bom estado geral. Icterícia leve. Dor à palpação em hipocôndrio direito. Temperatura: [X]°C. Sem peritonismo.",
  // ── ESÔFAGO / ESTÔMAGO ───────────────────────────────────────────────────
  "Doença do Refluxo Gastroesofágico (DRGE) — Fundoplicatura":
    "Bom estado geral. Abdômen plano, flácido, sem visceromegalias. Leve dor à palpação epigástrica. Sem sinais de alarme (disfagia progressiva, perda de peso, massa palpável). Exame físico sem alterações específicas.",
  "Hérnia Hiatal Mista / Paraesofágica":
    "Bom estado geral. Abdômen sem alterações à palpação. Sem sinais de complicações agudas. Ausculta cardiopulmonar sem alterações.",
  "Acalasia de Esôfago":
    "Estado geral [regular/bom], com perda de peso [X] kg. Abdômen sem alterações à palpação. Sem sinais de massa cervical ou supraclavicular.",
  "Divertículo de Zenker":
    "Bom estado geral. Pescoço sem massas palpáveis. Abdômen sem alterações. Sem sinais de aspiração pulmonar no exame físico.",
  "Úlcera Péptica Gástrica Refratária":
    "Bom estado geral. Abdômen plano, flácido. Dor à palpação profunda em epigástrio. Sem sinais de peritonismo ou perfuração. Ruídos hidroaéreos presentes.",
  "Úlcera Péptica Duodenal Refratária":
    "Bom estado geral. Dor à palpação em epigástrio e hipocôndrio direito. Sem defesa muscular. Ruídos hidroaéreos presentes.",
  "Tumor Benigno Gástrico (GIST / Leiomioma)":
    "Bom estado geral. Abdômen plano. Massa palpável em epigástrio / [localização] de [X] cm, de consistência [firme/amolecida], [móvel/fixa]. Sem sinais de peritonismo.",
  "Estenose Pilórica do Adulto":
    "Estado geral [regular]. Abdômen com distensão epigástrica. Ruídos de sucussão gástrica presentes. Peristaltismo visível em epigástrio após refeição. Desidratação [leve/moderada].",
  // ── INTESTINO DELGADO ─────────────────────────────────────────────────────
  "Aderências / Bridas Intestinais (cirurgia eletiva)":
    "Bom estado geral. Cicatriz cirúrgica abdominal anterior. Abdômen plano, flácido, sem distensão. Ruídos hidroaéreos normais. Sem sinais de obstrução no momento. Sem peritonismo.",
  "Doença de Crohn — Ressecção Eletiva":
    "Estado geral [bom/regular]. Abdômen com dor à palpação em fossa ilíaca direita / [localização]. Massa palpável em FID de [X] cm (plastrão inflamatório). Sem sinais de peritonismo agudo. Fístulas entero-cutâneas: [presentes/ausentes]. Perianal: [normal/alterado].",
  "Divertículo de Meckel Sintomático":
    "Bom estado geral. Abdômen sem distensão. Dor à palpação em mesogástrio / fossa ilíaca direita. Sem sinais de peritonismo. Sem massa palpável.",
  // ── CÓLON E RETO ─────────────────────────────────────────────────────────
  "Doença Diverticular do Cólon Sintomática":
    "Bom estado geral, afebril (fora de crise aguda). Abdômen com corda sigmoidiana palpável em fossa ilíaca esquerda, sensível à palpação profunda. Sem defesa muscular ou peritonismo. Ruídos hidroaéreos normais.",
  "Megacólon Chagásico":
    "Abdômen globoso e distendido. Timpanismo difuso à percussão. Ruídos hidroaéreos [diminuídos/aumentados]. Massa fecal palpável em flanco esquerdo e hipogástrio. Toque retal: ampola retal vazia / com fezes moldadas.",
  "Colite Ulcerativa — Cirurgia Eletiva":
    "Estado geral [regular/comprometido]. Abdômen com dor difusa à palpação. Sensibilidade aumentada em fossa ilíaca esquerda e hipogástrio. Distensão abdominal [leve/moderada]. Toque retal: [sangue/muco].",
  "Prolapso Retal":
    "Bom estado geral. Inspeção perianal: mucosa/parede retal exteriorizada ao esforço de [X] cm além da borda anal, de aspecto rosado/congestivo. Tônus esfincteriano [diminuído/normal]. Toque retal sem estenose.",
  // ── ANORRETAL ─────────────────────────────────────────────────────────────
  "Hemorróidas Grau III / IV":
    "Bom estado geral. Inspeção perianal: mamilos hemorroidários externos visíveis / prolapsados. Prolapso de mamilos internos ao esforço (grau III) / prolapso irreversível (grau IV). Toque retal: ampola retal livre, sem massas. Anuscopia: coxins hemorroidários internos aumentados em posições [horária].",
  "Fissura Anal Crônica":
    "Inspeção perianal: fissura anal [posterior/anterior] na linha média, com bordas fibróticas, exposição de fibras do esfíncter interno, sentinela cutânea e papila anal hipertrófica associadas. Espasmo esfincteriano evidenciado ao toque (toque limitado pela dor).",
  "Fístula Perianal (transesfincteriana / supraesfincteriana)":
    "Inspeção perianal: orifício externo de fístula a [X] cm da borda anal, na posição [horária], com discreto halo de tecido cicatricial. Cordão fibroso palpável no trajeto. Toque retal: orifício interno palpável na linha denteada. Tônus esfincteriano preservado.",
  "Fístula Perianal Baixa (interesfincteriana / submucosa)":
    "Inspeção perianal: orifício externo de fístula a [X] cm da borda anal. Cordão fibroso superficial palpável. Toque retal: tônus preservado, orifício interno identificável.",
  "Abscesso Anorretal Recorrente":
    "Região perianal com hiperemia, edema e flutuação em [posição]. Toque retal: dor à palpação. Temperatura: [X]°C.",
  "Cisto Pilonidal / Seio Pilonidal":
    "Inspeção da região sacrococcígea: [orifícios/óstios] pilonidais na linha média, com secreção seropurulenta. Área de fibrose/cicatriz por episódios prévios. Sem sinais de infecção aguda no momento.",
  // ── FÍGADO / PÂNCREAS / BAÇO ──────────────────────────────────────────────
  "Cisto Hepático Simples Sintomático":
    "Bom estado geral. Abdômen com leve dor à palpação em hipocôndrio direito. Hepatomegalia de [X] cm abaixo do rebordo costal / massa palpável. Sem icterícia ou ascite.",
  "Esplenomegalia — Esplenectomia Eletiva":
    "Bom estado geral. Abdômen com esplenomegalia palpável a [X] cm do rebordo costal esquerdo, de consistência [firme/amolecida], superfície regular. Sem dor aguda. Sem ascite.",
  "Pseudocisto Pancreático Sintomático":
    "Estado geral [bom/regular]. Abdômen com massa palpável em epigástrio / mesogástrio, de consistência cística, sensível à palpação. Ruídos hidroaéreos presentes. Sem sinais de peritonismo.",
  "Pancreatite Crônica — Cirurgia Eletiva (Frey / Puestow / Beger)":
    "Estado geral [regular], emagrecido. Abdômen com dor à palpação em epigástrio, sem peritonismo. Esteatorreia referida. Sem icterícia no momento.",
  // ── TIREOIDE ──────────────────────────────────────────────────────────────
  "Bócio Nodular — Tireoidectomia Parcial / Total":
    "Bom estado geral. Pescoço com aumento do volume tireoidiano, visível em posição ortostática. À palpação: bócio [difuso/multinodular], consistência [firme/amolecida], superfície [irregular], sem dor. Nódulo dominante em lobo [D/E] de [X] cm. Linfonodos cervicais: não palpáveis. Sem disfagia ou disfonia referida ao exame.",
  "Nódulo de Tireoide Indeterminado (Bethesda III / IV)":
    "Bom estado geral. Tireoide com nódulo palpável em lobo [D/E], de [X] cm, consistência [firme/amolecida], superfície regular, sem dor. Sem linfonodomegalia cervical. Sem sinais de hiper ou hipotireoidismo ao exame.",
  "Hipertireoidismo Refratário ao Tratamento Clínico":
    "Estado geral [bom/regular]. Tireoide difusamente aumentada / nodular, consistência amolecida, sopro audível [presente/ausente]. Tremor fino de extremidades. Taquicardia (FC: [X] bpm). Pele quente e úmida. Exoftalmia [ausente/presente].",
  "Hiperparatireoidismo Primário — Paratireoidectomia":
    "Bom estado geral. Pescoço sem massas palpáveis visíveis. Região cervical anterior sem alterações. Sem dor óssea à compressão no momento.",
  "Adenoma de Paratireoide":
    "Exame físico do pescoço sem alterações palpáveis. Região cervical sem massas. Sem sinais de hipercalcemia grave (fraqueza muscular, confusão mental).",
  // ── MAMA ──────────────────────────────────────────────────────────────────
  "Fibroadenoma de Mama":
    "Mamas simétricas, sem alterações cutâneas ou retração mamilar. À palpação: nódulo em mama [D/E], quadrante [X], de [X] cm, consistência elástica/firme, superfície regular, bem delimitado, móvel, indolor. Axilas livres de linfonodos palpáveis.",
  "Tumor Filodes Benigno de Mama":
    "Mama [D/E] com aumento de volume. Nódulo de [X] cm, consistência firme, lobulado, superfície irregular, móvel. Sem alterações cutâneas (pele de laranja, retração). Axila livre.",
  "Ginecomastia":
    "Aumento de tecido glandular subareolar bilateral / unilateral em [D/E], de [X] cm, consistência glandular (diferencia-se de lipomastia). Sem nódulos suspeitos, retração mamilar ou descarga papilar.",
  "Abscesso Mamário Recorrente / Fístula de Ducto":
    "Região periareolar com fístula de orifício a [X] cm do mamilo, com secreção [purulenta/serosa]. Área de fibrose periareolar. Mamilo com [inversão/desvio]. Sem linfonodomegalia axilar.",
  // ── PARTES MOLES / DERMATOLOGIA ──────────────────────────────────────────
  "Cisto Sebáceo / Epidérmico":
    "Nódulo subcutâneo em [localização], de [X] cm, superfície lisa, consistência cística/amolecida, flutuante, bem delimitado, móvel em relação aos planos profundos. Orifício central (ponto negro) presente. Sem sinais flogísticos ativos (sem hiperemia, edema ou dor intensa). Pele suprajacente íntegra / com alterações pós-infecção.",
  "Lipoma":
    "Nódulo subcutâneo em [localização], de [X] cm, de consistência amolecida, superfície lobulada, bem delimitado, indolor, móvel em planos superficiais. Sem aderência a planos profundos. Pele suprajacente sem alterações.",
  "Fibroma / Dermatofibroma":
    "Nódulo cutâneo/subcutâneo em [localização], de [X] cm, firme, aderido à derme (sinal do dimple positivo no dermatofibroma), sem sinais inflamatórios. Indolor à palpação.",
  "Nevo Melanocítico — Exérese Eletiva":
    "Lesão pigmentada em [localização], de [X] × [X] mm, bordas [irregulares/regulares], coloração [marrom/enegrecida/heterogênea]. Critérios ABCDE: A [assimetria], B [bordas], C [cor], D [diâmetro > 6 mm], E [evolução]. Sem ulceração ou sangramento ativo. Linfonodos regionais não palpáveis.",
  "Carcinoma Basocelular / Espinocelular (ressecção eletiva)":
    "Lesão cutânea em [localização], de [X] mm, pérola/ulcerada/queratótica, bordas [elevadas/irregulares], sem sangramento ativo no momento. Sem linfonodomegalia regional palpável. Sem metástases à distância identificadas clinicamente.",
  "Condiloma Acuminado Perianal (extenso)":
    "Inspeção perianal: múltiplas lesões verrucosas, vegetantes, de coloração rósea/acastanhada, confluentes, cobrindo [X]% da região perianal. Sem necrose ou sangramento ativo. Toque retal: lesões intranais [presentes/ausentes].",
  "Cisto Pilonidal / Seio Pilonidal":
    "Inspeção da região sacrococcígea: óstios pilonidais na linha média com secreção. Área de fibrose. Sem sinais de infecção aguda.",
  "Hidradenite Supurativa Perianal":
    "Inspeção perianal e perineal: lesões nodulares, abscessos, trajetos fistulosos e cicatrizes retráteis em região [inguinal/perianal/perineal]. Secreção purulenta. Grau de Hurley: [I/II/III].",
};

const getExameFisico = (motivo) => {
  if (EXAME_FISICO_POR_MOTIVO[motivo]) return EXAME_FISICO_POR_MOTIVO[motivo];
  return `Bom estado geral, corado, hidratado, afebril. PA: [X] mmHg. FC: [X] bpm. Peso: [X] kg.\nAbdômen [plano/globoso], flácido, sem visceromegalias, sem sinais de peritonismo. Ruídos hidroaéreos presentes e normais.\nExame dirigido para ${motivo}: [descrever achados relevantes]. Sem alterações agudas no momento.`;
};

const COMORBIDADES = [
  { id: "has", label: "Hipertensão Arterial Sistêmica (HAS)" },
  { id: "dm", label: "Diabetes Mellitus (DM)" },
  { id: "cardiopatia", label: "Cardiopatia" },
  { id: "pneumopatia", label: "Pneumopatia" },
  { id: "nefropatia", label: "Nefropatia" },
  { id: "obesidade", label: "Obesidade" },
  { id: "alergia", label: "Alergia a Medicamentos" },
  { id: "drogas", label: "Uso de Drogas Ilícitas" },
  { id: "tabagismo", label: "Tabagismo" },
  { id: "etilismo", label: "Etilismo" },
  { id: "sem_comorbidades", label: "Sem Comorbidades Conhecidas" },
];

const MEDICAMENTOS_POR_COMORBIDADE = {
  has: {
    titulo: "Hipertensão Arterial (HAS)",
    grupos: [
      {
        grupo: "IECA / BRA",
        medicamentos: [
          "Enalapril 5mg 1x/dia",
          "Enalapril 10mg 2x/dia",
          "Losartana 50mg 1x/dia",
          "Losartana 100mg 1x/dia",
          "Ramipril 5mg 1x/dia",
          "Valsartana 80mg 1x/dia",
        ],
      },
      {
        grupo: "Bloqueadores do Canal de Cálcio",
        medicamentos: [
          "Anlodipino 5mg 1x/dia",
          "Anlodipino 10mg 1x/dia",
          "Nifedipino retard 20mg 2x/dia",
        ],
      },
      {
        grupo: "Betabloqueadores",
        medicamentos: [
          "Atenolol 25mg 1x/dia",
          "Atenolol 50mg 1x/dia",
          "Metoprolol 50mg 2x/dia",
          "Carvedilol 6,25mg 2x/dia",
          "Carvedilol 12,5mg 2x/dia",
        ],
      },
      {
        grupo: "Diuréticos",
        medicamentos: [
          "Hidroclorotiazida 25mg 1x/dia",
          "Clortalidona 25mg 1x/dia",
          "Furosemida 40mg 1x/dia",
          "Espironolactona 25mg 1x/dia",
        ],
      },
    ],
  },
  dm: {
    titulo: "Diabetes Mellitus (DM)",
    grupos: [
      {
        grupo: "Biguanidas",
        medicamentos: [
          "Metformina 500mg 2x/dia",
          "Metformina 850mg 2x/dia",
          "Metformina 1g 2x/dia",
        ],
      },
      {
        grupo: "Sulfonilureias",
        medicamentos: [
          "Glibenclamida 5mg 1x/dia",
          "Glicazida 30mg 1x/dia",
          "Glipizida 5mg 1x/dia",
        ],
      },
      {
        grupo: "Inibidores de DPP-4 / GLP-1",
        medicamentos: [
          "Sitagliptina 100mg 1x/dia",
          "Vildagliptina 50mg 2x/dia",
          "Liraglutida 1,2mg SC 1x/dia",
          "Semaglutida 0,5mg SC 1x/semana",
        ],
      },
      {
        grupo: "Inibidores de SGLT-2",
        medicamentos: [
          "Empagliflozina 10mg 1x/dia",
          "Dapagliflozina 10mg 1x/dia",
        ],
      },
      {
        grupo: "Insulinas",
        medicamentos: [
          "Insulina NPH 10UI SC 2x/dia",
          "Insulina Regular conforme glicemia",
          "Insulina Glargina 10UI SC 1x/dia",
          "Insulina Detemir SC 1x/dia",
        ],
      },
    ],
  },
  cardiopatia: {
    titulo: "Cardiopatia",
    grupos: [
      {
        grupo: "Antiagregantes / Anticoagulantes",
        medicamentos: [
          "AAS 100mg 1x/dia",
          "Clopidogrel 75mg 1x/dia",
          "Warfarina (dose variável — INR alvo 2–3)",
          "Rivaroxabana 20mg 1x/dia",
          "Apixabana 5mg 2x/dia",
          "Dabigatrana 150mg 2x/dia",
        ],
      },
      {
        grupo: "Hipolipemiantes",
        medicamentos: [
          "Atorvastatina 20mg 1x/dia",
          "Atorvastatina 40mg 1x/dia",
          "Atorvastatina 80mg 1x/dia",
          "Rosuvastatina 10mg 1x/dia",
          "Rosuvastatina 20mg 1x/dia",
        ],
      },
      {
        grupo: "Betabloqueadores / Antiarrítmicos",
        medicamentos: [
          "Metoprolol 50mg 2x/dia",
          "Carvedilol 6,25mg 2x/dia",
          "Bisoprolol 5mg 1x/dia",
          "Amiodarona 200mg 1x/dia",
          "Digoxina 0,25mg 1x/dia",
        ],
      },
      {
        grupo: "Para IC / Vasodilatadores",
        medicamentos: [
          "Sacubitril/Valsartana 49/51mg 2x/dia",
          "Ivabradina 5mg 2x/dia",
          "Isossorbida 20mg 3x/dia",
          "Furosemida 40mg 1x/dia",
          "Espironolactona 25mg 1x/dia",
        ],
      },
    ],
  },
  pneumopatia: {
    titulo: "Pneumopatia",
    grupos: [
      {
        grupo: "Broncodilatadores de Curta Ação (SABA)",
        medicamentos: [
          "Salbutamol 100mcg inalatório (2 jatos SOS)",
          "Fenoterol 100mcg inalatório (2 jatos SOS)",
        ],
      },
      {
        grupo: "Broncodilatadores de Longa Ação (LABA/LAMA)",
        medicamentos: [
          "Formoterol 12mcg inalatório 2x/dia",
          "Salmeterol 50mcg inalatório 2x/dia",
          "Tiotrópio 18mcg inalatório 1x/dia",
          "Umeclidínio 62,5mcg inalatório 1x/dia",
        ],
      },
      {
        grupo: "Corticosteroides Inalatórios",
        medicamentos: [
          "Budesonida 200mcg inalatório 2x/dia",
          "Budesonida 400mcg inalatório 2x/dia",
          "Fluticasona 250mcg inalatório 2x/dia",
          "Beclometasona 200mcg inalatório 2x/dia",
        ],
      },
      {
        grupo: "Corticosteroides Sistêmicos / Outros",
        medicamentos: [
          "Prednisona 20mg 1x/dia (exacerbação)",
          "Montelucaste 10mg 1x/dia",
          "Teofilina 200mg 2x/dia",
        ],
      },
    ],
  },
  nefropatia: {
    titulo: "Nefropatia",
    grupos: [
      {
        grupo: "Protetores Renais",
        medicamentos: [
          "Losartana 50mg 1x/dia",
          "Enalapril 10mg 1x/dia",
          "Dapagliflozina 10mg 1x/dia",
        ],
      },
      {
        grupo: "Anemia / Osso",
        medicamentos: [
          "Eritropoetina 4.000UI SC 3x/semana",
          "Ferro sacarato IV (conforme protocolo)",
          "Carbonato de cálcio 500mg 3x/dia",
          "Calcitriol 0,25mcg 1x/dia",
        ],
      },
      {
        grupo: "Diuréticos / Equilíbrio",
        medicamentos: [
          "Furosemida 40mg 1x/dia",
          "Furosemida 80mg 2x/dia",
          "Bicarbonato de sódio 840mg 3x/dia",
        ],
      },
      {
        grupo: "Quelantes de Fósforo",
        medicamentos: [
          "Sevelâmer 800mg 3x/dia (com refeições)",
          "Carbonato de cálcio como quelante 3x/dia",
        ],
      },
    ],
  },
  obesidade: {
    titulo: "Obesidade",
    grupos: [
      {
        grupo: "Antiobesidade",
        medicamentos: [
          "Orlistate 120mg 3x/dia (com refeições)",
          "Sibutramina 10mg 1x/dia",
          "Liraglutida 3mg SC 1x/dia",
          "Semaglutida 2,4mg SC 1x/semana",
          "Naltrexona/Bupropiona 8/90mg 2x/dia",
        ],
      },
      {
        grupo: "Adjuvantes Metabólicos",
        medicamentos: [
          "Metformina 850mg 2x/dia",
          "Topiramato 25mg 1x/dia",
        ],
      },
    ],
  },
  tabagismo: {
    titulo: "Tabagismo",
    grupos: [
      {
        grupo: "Terapia de Reposição de Nicotina",
        medicamentos: [
          "Adesivo de nicotina 21mg/24h (fase 1)",
          "Adesivo de nicotina 14mg/24h (fase 2)",
          "Goma de nicotina 2mg SOS",
          "Pastilha de nicotina 2mg SOS",
        ],
      },
      {
        grupo: "Farmacoterapia",
        medicamentos: [
          "Vareniclina 0,5mg 1x/dia (1ª semana) → 1mg 2x/dia",
          "Bupropiona 150mg 1x/dia → 2x/dia",
        ],
      },
    ],
  },
  etilismo: {
    titulo: "Etilismo",
    grupos: [
      {
        grupo: "Redução do Craving / Abstinência",
        medicamentos: [
          "Naltrexona 50mg 1x/dia",
          "Acamprosato 666mg 3x/dia",
          "Dissulfiram 250mg 1x/dia (uso supervisionado)",
        ],
      },
      {
        grupo: "Suplementação",
        medicamentos: [
          "Tiamina (Vitamina B1) 300mg/dia VO",
          "Complexo B 1 comprimido 2x/dia",
          "Ácido fólico 5mg 1x/dia",
        ],
      },
      {
        grupo: "Controle de Abstinência Aguda",
        medicamentos: [
          "Diazepam 10mg VO (protocolo CIWA)",
          "Lorazepam 2mg VO (protocolo CIWA)",
        ],
      },
    ],
  },
  drogas: {
    titulo: "Uso de Drogas Ilícitas",
    grupos: [
      {
        grupo: "Opioides (Redução de Danos / TAO)",
        medicamentos: [
          "Metadona (dose conforme protocolo TAO)",
          "Buprenorfina/Naloxona 8/2mg sublingual",
        ],
      },
      {
        grupo: "Suporte Psiquiátrico",
        medicamentos: [
          "Quetiapina 25mg à noite (agitação/insônia)",
          "Haloperidol 5mg IM (crise aguda)",
          "Diazepam 10mg VO (abstinência)",
        ],
      },
    ],
  },
};

function ModalMedicamentos({ comorbidade, open, onClose, onConfirmar }) {
  const [selecionados, setSelecionados] = useState([]);
  const dados = MEDICAMENTOS_POR_COMORBIDADE[comorbidade?.id];

  const toggle = (med) =>
    setSelecionados((prev) =>
      prev.includes(med) ? prev.filter((m) => m !== med) : [...prev, med]
    );

  const handleConfirmar = () => {
    onConfirmar(selecionados);
    setSelecionados([]);
    onClose();
  };

  const handleClose = () => {
    setSelecionados([]);
    onClose();
  };

  if (!dados) return null;

  return (
    <Dialog open={open} onOpenChange={(v) => !v && handleClose()}>
      <DialogContent className="max-w-lg max-h-[80vh] overflow-y-auto">
        <DialogHeader>
          <DialogTitle className="flex items-center gap-2 text-teal-700">
            <Pill className="w-5 h-5" />
            Medicamentos — {dados.titulo}
          </DialogTitle>
          <p className="text-sm text-gray-500 pt-1">
            Selecione os medicamentos que o paciente usa para adicionar ao campo de medicações.
          </p>
        </DialogHeader>

        <div className="space-y-4 py-2">
          {dados.grupos.map((g) => (
            <div key={g.grupo}>
              <Badge variant="secondary" className="mb-2 text-xs font-semibold">
                {g.grupo}
              </Badge>
              <div className="space-y-1 pl-1">
                {g.medicamentos.map((med) => (
                  <div key={med} className="flex items-center gap-2">
                    <Checkbox
                      id={`med-${med}`}
                      checked={selecionados.includes(med)}
                      onCheckedChange={() => toggle(med)}
                    />
                    <label
                      htmlFor={`med-${med}`}
                      className="text-sm text-gray-700 cursor-pointer select-none"
                    >
                      {med}
                    </label>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>

        <DialogFooter className="gap-2">
          <Button variant="outline" onClick={handleClose}>
            Fechar
          </Button>
          <Button
            onClick={handleConfirmar}
            disabled={selecionados.length === 0}
            className="bg-teal-600 hover:bg-teal-700 text-white"
          >
            Adicionar {selecionados.length > 0 ? `(${selecionados.length})` : ""} ao formulário
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}

function CopyButton({ text, label }) {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <Button
      onClick={handleCopy}
      size="sm"
      className={`transition-all duration-300 ${
        copied
          ? "bg-gray-500 hover:bg-gray-600"
          : "bg-teal-600 hover:bg-teal-700"
      } text-white`}
    >
      {copied ? (
        <>
          <CheckCircle className="w-4 h-4 mr-1" />
          Copiado!
        </>
      ) : (
        <>
          <Copy className="w-4 h-4 mr-1" />
          {label || "Copiar"}
        </>
      )}
    </Button>
  );
}

function OutputCard({ icon: Icon, title, content, iconColor }) {
  if (!content) return null;
  return (
    <Card className="border border-gray-200 shadow-sm">
      <CardHeader className="pb-2 pt-4 px-4">
        <CardTitle className="text-base font-semibold flex items-center gap-2 text-gray-700">
          <Icon className={`w-5 h-5 ${iconColor}`} />
          {title}
        </CardTitle>
      </CardHeader>
      <CardContent className="px-4 pb-4">
        <Textarea
          value={content}
          readOnly
          rows={8}
          className="w-full font-mono text-sm bg-gray-50 resize-y"
        />
        <div className="mt-2 flex justify-end">
          <CopyButton text={content} />
        </div>
      </CardContent>
    </Card>
  );
}

export default function GeradorLaudo() {
  const hoje = new Date().toLocaleDateString("pt-BR");

  const [form, setForm] = useState({
    motivoPrincipal: "",
    motivoPersonalizado: "",
    motivoAssociado: "",
    procedimento: "",
    procedimentoCustom: "",
    anamnese: "",
    exame: "",
    alergias: "",
    medicacoes: "",
    conduta: "",
    comorbidades: {},
  });

  const [outputs, setOutputs] = useState(null);
  const [modalComorbidade, setModalComorbidade] = useState(null);

  const set = (key, val) => setForm((prev) => ({ ...prev, [key]: val }));

  const toggleComorbidade = (id) => {
    const jaMarcada = !!form.comorbidades[id];

    setForm((prev) => {
      const next = { ...prev.comorbidades };
      if (id === "sem_comorbidades") {
        if (next[id]) {
          delete next[id];
        } else {
          return { ...prev, comorbidades: { sem_comorbidades: true } };
        }
      } else {
        if (next[id]) {
          delete next[id];
        } else {
          delete next["sem_comorbidades"];
          next[id] = true;
        }
      }
      return { ...prev, comorbidades: next };
    });

    // Abre modal ao marcar (não ao desmarcar), se houver medicamentos para essa comorbidade
    if (!jaMarcada && id !== "sem_comorbidades" && MEDICAMENTOS_POR_COMORBIDADE[id]) {
      setModalComorbidade(COMORBIDADES.find((c) => c.id === id));
    }
  };

  const adicionarMedicamentos = (lista) => {
    if (lista.length === 0) return;
    setForm((prev) => {
      const atual = prev.medicacoes.trim();
      const novo = lista.join("\n");
      return { ...prev, medicacoes: atual ? `${atual}\n${novo}` : novo };
    });
  };

  const comorbidadesText = () => {
    const selecionadas = COMORBIDADES.filter((c) => form.comorbidades[c.id]).map((c) => c.label);
    return selecionadas.length > 0 ? selecionadas.join(", ") : "Sem comorbidades conhecidas";
  };

  const motivoPrincipalText = () =>
    form.motivoPersonalizado || form.motivoPrincipal || "[motivo não informado]";

  const gerarLaudo = () => {
    const motivo = motivoPrincipalText();
    const associado = (form.motivoAssociado && form.motivoAssociado !== "none") ? `\nMotivo Associado: ${form.motivoAssociado}` : "";
    const procedimento = (form.procedimento === "__custom__" ? form.procedimentoCustom : form.procedimento) || "[procedimento não informado]";
    const anamnese = form.anamnese || "[anamnese não informada]";
    const exame = form.exame || "[exame físico não informado]";
    const comorbidades = comorbidadesText();
    const alergias = form.alergias || "Nega";
    const medicacoes = form.medicacoes || "Nega uso de medicações";
    const conduta = form.conduta || "[conduta não informada]";

    const laudo = `LAUDO DE CONSULTA CIRÚRGICA
Data: ${hoje}
Médico: Dr. Claudio M Orenstein — CRM-SP 58120

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MOTIVO DO ENCAMINHAMENTO
${motivo}${associado}

PROCEDIMENTO PROPOSTO
${procedimento}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ANAMNESE / QUEIXA PRINCIPAL
${anamnese}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ANTECEDENTES E COMORBIDADES
${comorbidades}

Alergias: ${alergias}
Medicações em uso: ${medicacoes}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXAME FÍSICO
${exame}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONDUTA / RECOMENDAÇÕES
${conduta}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dr. Claudio M Orenstein
CRM-SP 58120`;

    const preAnestesica = `SOLICITAÇÃO DE AVALIAÇÃO PRÉ-ANESTÉSICA
Data: ${hoje}

Encaminho paciente para avaliação pré-anestésica visando cirurgia eletiva.

Diagnóstico / Motivo: ${motivo}${associado ? `\n${associado}` : ""}
Procedimento Proposto: ${procedimento}

Comorbidades: ${comorbidades}
Alergias: ${alergias}
Medicações em uso: ${medicacoes}

${anamnese ? `Histórico Resumido:\n${anamnese}` : ""}

Solicito avaliação quanto ao risco anestésico-cirúrgico e liberação para o procedimento.

Dr. Claudio M Orenstein — CRM-SP 58120`;

    const cardiologia = `SOLICITAÇÃO DE AVALIAÇÃO CARDIOLÓGICA PRÉ-OPERATÓRIA
Data: ${hoje}

Encaminho paciente para avaliação cardiológica pré-operatória.

Diagnóstico: ${motivo}
Procedimento Proposto: ${procedimento}

Comorbidades: ${comorbidades}
Alergias: ${alergias}
Medicações em uso: ${medicacoes}

Solicito avaliação do risco cardiovascular e liberação para cirurgia eletiva.

Dr. Claudio M Orenstein — CRM-SP 58120`;

    const pneumologia = `SOLICITAÇÃO DE AVALIAÇÃO PNEUMOLÓGICA PRÉ-OPERATÓRIA
Data: ${hoje}

Encaminho paciente para avaliação pneumológica pré-operatória.

Diagnóstico: ${motivo}
Procedimento Proposto: ${procedimento}

Comorbidades: ${comorbidades}
Alergias: ${alergias}
Medicações em uso: ${medicacoes}

Solicito avaliação do risco respiratório e liberação para cirurgia eletiva.

Dr. Claudio M Orenstein — CRM-SP 58120`;

    const aih = `DADOS PARA AIH — Autorização de Internação Hospitalar
Data: ${hoje}

Diagnóstico Principal: ${motivo}${associado ? `\nDiagnóstico Secundário: ${associado}` : ""}
Procedimento Proposto: ${procedimento}

Comorbidades: ${comorbidades}
Medicações: ${medicacoes}
Alergias: ${alergias}

Conduta: ${conduta}

Médico Solicitante: Dr. Claudio M Orenstein
CRM-SP 58120`;

    setOutputs({ laudo, preAnestesica, cardiologia, pneumologia, aih });

    setTimeout(() => {
      document.getElementById("outputs-section")?.scrollIntoView({ behavior: "smooth" });
    }, 100);
  };

  const limpar = () => {
    setForm({
      motivoPrincipal: "",
      motivoPersonalizado: "",
      motivoAssociado: "",
      procedimento: "",
      procedimentoCustom: "",
      anamnese: "",
      exame: "",
      alergias: "",
      medicacoes: "",
      conduta: "",
      comorbidades: {},
    });
    setOutputs(null);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 p-4 sm:p-8">
      <div className="max-w-4xl mx-auto space-y-6">
        {/* Header */}
        <div className="bg-gradient-to-r from-teal-600 to-cyan-700 rounded-2xl p-6 text-white shadow-lg">
          <div className="flex items-center justify-center gap-3 mb-2">
            <Stethoscope className="w-8 h-8" />
            <h1 className="text-2xl sm:text-3xl font-extrabold tracking-tight">
              Gerador de Laudos — Cirurgia Eletiva
            </h1>
          </div>
          <p className="text-center text-sm opacity-90">
            Preencha os dados do paciente e gere laudos, avaliações e AIH automaticamente.
          </p>
        </div>

        {/* Formulário */}
        <Card className="shadow-xl">
          <CardHeader className="border-b pb-4">
            <CardTitle className="text-lg text-gray-800 flex items-center gap-2">
              <ClipboardList className="w-5 h-5 text-teal-600" />
              Dados do Encaminhamento
            </CardTitle>
          </CardHeader>
          <CardContent className="pt-6 space-y-6">
            {/* Motivo Principal */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div className="space-y-1">
                <Label>Motivo do Encaminhamento Principal *</Label>
                <Select
                  value={form.motivoPrincipal}
                  onValueChange={(v) => {
                    const opcoes = PROCEDIMENTOS_POR_MOTIVO[v] || [];
                    setForm((prev) => ({
                      ...prev,
                      motivoPrincipal: v,
                      procedimento: opcoes[0] || prev.procedimento,
                      procedimentoCustom: "",
                    }));
                  }}
                >
                  <SelectTrigger>
                    <SelectValue placeholder="Selecione..." />
                  </SelectTrigger>
                  <SelectContent className="max-h-72">
                    {MOTIVOS_GRUPOS.map((g) => (
                      <SelectGroup key={g.grupo}>
                        <SelectLabel className="text-xs font-bold text-teal-700 bg-teal-50 px-2 py-1">
                          {g.grupo}
                        </SelectLabel>
                        {g.opcoes.map((m) => (
                          <SelectItem key={m} value={m}>
                            {m}
                          </SelectItem>
                        ))}
                      </SelectGroup>
                    ))}
                  </SelectContent>
                </Select>
              </div>
              <div className="space-y-1">
                <Label>Motivo Personalizado (sobrescreve o campo acima)</Label>
                <Input
                  placeholder="Ex: Hérnia de Spiegel direita..."
                  value={form.motivoPersonalizado}
                  onChange={(e) => set("motivoPersonalizado", e.target.value)}
                />
              </div>
            </div>

            {/* Motivo Associado */}
            <div className="space-y-1">
              <Label>Motivo Associado (Opcional)</Label>
              <Select
                value={form.motivoAssociado}
                onValueChange={(v) => set("motivoAssociado", v)}
              >
                <SelectTrigger>
                  <SelectValue placeholder="Selecione diagnóstico secundário..." />
                </SelectTrigger>
                <SelectContent className="max-h-72">
                  <SelectItem value="none">Nenhum</SelectItem>
                  {MOTIVOS_GRUPOS.map((g) => (
                    <SelectGroup key={g.grupo}>
                      <SelectLabel className="text-xs font-bold text-teal-700 bg-teal-50 px-2 py-1">
                        {g.grupo}
                      </SelectLabel>
                      {g.opcoes.map((m) => (
                        <SelectItem key={m} value={m}>
                          {m}
                        </SelectItem>
                      ))}
                    </SelectGroup>
                  ))}
                </SelectContent>
              </Select>
            </div>

            {/* Procedimento */}
            <div className="space-y-2">
              <Label>Procedimento Proposto</Label>
              {form.motivoPrincipal && PROCEDIMENTOS_POR_MOTIVO[form.motivoPrincipal] ? (
                <Select
                  value={form.procedimento}
                  onValueChange={(v) => {
                    set("procedimento", v);
                    set("procedimentoCustom", "");
                  }}
                >
                  <SelectTrigger>
                    <SelectValue placeholder="Selecione o procedimento..." />
                  </SelectTrigger>
                  <SelectContent className="max-h-72">
                    {PROCEDIMENTOS_POR_MOTIVO[form.motivoPrincipal].map((p) => (
                      <SelectItem key={p} value={p}>
                        {p}
                      </SelectItem>
                    ))}
                    <SelectItem value="__custom__">
                      ✏️ Digitar procedimento personalizado...
                    </SelectItem>
                  </SelectContent>
                </Select>
              ) : (
                <Input
                  placeholder="Ex: Herniorrafia inguinal direita com tela (técnica de Lichtenstein)"
                  value={form.procedimento}
                  onChange={(e) => set("procedimento", e.target.value)}
                />
              )}
              {form.procedimento === "__custom__" && (
                <Input
                  autoFocus
                  placeholder="Descreva o procedimento proposto..."
                  value={form.procedimentoCustom}
                  onChange={(e) => set("procedimentoCustom", e.target.value)}
                  className="mt-1"
                />
              )}
            </div>

            {/* Anamnese */}
            <div className="space-y-1">
              <div className="flex items-center justify-between">
                <Label>Anamnese / Queixa Principal</Label>
                {form.motivoPrincipal && (
                  <Button
                    type="button"
                    size="sm"
                    variant="outline"
                    className="text-teal-700 border-teal-300 hover:bg-teal-50 h-7 px-3 text-xs font-semibold"
                    onClick={() => {
                      const proc = form.procedimento === "__custom__"
                        ? form.procedimentoCustom
                        : form.procedimento;
                      set("anamnese", getAnamnese(form.motivoPrincipal, proc));
                    }}
                  >
                    <Pill className="w-3 h-3 mr-1" />
                    Gerar anamnese
                  </Button>
                )}
              </div>
              <Textarea
                placeholder="Descreva a queixa principal e histórico clínico..."
                rows={5}
                value={form.anamnese}
                onChange={(e) => set("anamnese", e.target.value)}
              />
              {form.anamnese && (
                <p className="text-xs text-gray-400">
                  Revise e personalize os campos entre colchetes [ ] com os dados do paciente.
                </p>
              )}
            </div>

            {/* Comorbidades */}
            <div className="space-y-2">
              <Label className="text-base font-semibold">Comorbidades</Label>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 border rounded-lg p-4 bg-gray-50">
                {COMORBIDADES.map((c) => (
                  <div key={c.id} className="flex items-center gap-2">
                    <Checkbox
                      id={c.id}
                      checked={!!form.comorbidades[c.id]}
                      onCheckedChange={() => toggleComorbidade(c.id)}
                    />
                    <label
                      htmlFor={c.id}
                      className="text-sm text-gray-700 cursor-pointer select-none"
                    >
                      {c.label}
                    </label>
                  </div>
                ))}
              </div>
            </div>

            {/* Alergias + Medicações */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div className="space-y-1">
                <Label>Alergias Medicamentosas</Label>
                <Input
                  placeholder="Ex: Dipirona, Penicilina..."
                  value={form.alergias}
                  onChange={(e) => set("alergias", e.target.value)}
                />
              </div>
              <div className="space-y-1">
                <Label>Medicações em Uso</Label>
                <Textarea
                  placeholder="Ex: Losartana 50mg 1x/dia, Metformina 500mg 2x/dia..."
                  rows={3}
                  value={form.medicacoes}
                  onChange={(e) => set("medicacoes", e.target.value)}
                />
              </div>
            </div>

            {/* Exame Físico */}
            <div className="space-y-1">
              <div className="flex items-center justify-between">
                <Label>Exame Físico</Label>
                {form.motivoPrincipal && (
                  <Button
                    type="button"
                    size="sm"
                    variant="outline"
                    className="text-teal-700 border-teal-300 hover:bg-teal-50 h-7 px-3 text-xs font-semibold"
                    onClick={() => set("exame", getExameFisico(form.motivoPrincipal))}
                  >
                    <Pill className="w-3 h-3 mr-1" />
                    Gerar exame físico
                  </Button>
                )}
              </div>
              <Textarea
                placeholder="Descreva os achados do exame físico..."
                rows={5}
                value={form.exame}
                onChange={(e) => set("exame", e.target.value)}
              />
              {form.exame && (
                <p className="text-xs text-gray-400">
                  Revise e personalize os campos entre colchetes [ ] com os dados do paciente.
                </p>
              )}
            </div>

            {/* Conduta */}
            <div className="space-y-1">
              <Label>Conduta / Recomendações</Label>
              <Textarea
                placeholder="Descreva a conduta proposta e orientações..."
                rows={3}
                value={form.conduta}
                onChange={(e) => set("conduta", e.target.value)}
              />
            </div>

            {/* Ações */}
            <div className="flex flex-wrap gap-3 pt-4 border-t">
              <Button
                onClick={gerarLaudo}
                className="bg-teal-600 hover:bg-teal-700 text-white font-bold px-6 py-3 shadow-md transition-all duration-300 hover:scale-105"
              >
                <FileText className="w-5 h-5 mr-2" />
                Gerar Laudo
              </Button>
              <Button
                onClick={limpar}
                variant="destructive"
                className="px-6 py-3 font-bold shadow-md"
              >
                <Trash2 className="w-5 h-5 mr-2" />
                Limpar Formulário
              </Button>
            </div>
          </CardContent>
        </Card>

        {/* Outputs */}
        {outputs && (
          <div id="outputs-section" className="space-y-4">
            <h2 className="text-xl font-bold text-gray-800 border-b pb-2">
              Documentos Gerados
            </h2>

            <OutputCard
              icon={FileText}
              iconColor="text-teal-600"
              title="Laudo de Consulta Cirúrgica"
              content={outputs.laudo}
            />
            <OutputCard
              icon={Stethoscope}
              iconColor="text-purple-600"
              title="Solicitação Pré-Anestésica"
              content={outputs.preAnestesica}
            />
            <OutputCard
              icon={Heart}
              iconColor="text-red-500"
              title="Avaliação Cardiológica Pré-Operatória"
              content={outputs.cardiologia}
            />
            <OutputCard
              icon={Wind}
              iconColor="text-blue-500"
              title="Avaliação Pneumológica Pré-Operatória"
              content={outputs.pneumologia}
            />
            <OutputCard
              icon={ClipboardList}
              iconColor="text-amber-600"
              title="Dados para AIH"
              content={outputs.aih}
            />
          </div>
        )}
      </div>

      <ModalMedicamentos
        comorbidade={modalComorbidade}
        open={!!modalComorbidade}
        onClose={() => setModalComorbidade(null)}
        onConfirmar={adicionarMedicamentos}
      />
    </div>
  );
}

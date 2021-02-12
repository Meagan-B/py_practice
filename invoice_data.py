inv_2020_00 = ['INVOICE NUM', 'CLIENT NAME', 'PHONE', 'PROJECT DETAILS', 'DATE', 'TOTAL', 'PAID']
inv_2020_01 = ['001', 'Rick Brandt Photography', 'Grier day in the life (2 videos)', '12-10-2019','1000.00', '1000.00']
inv_2020_02 = ['002', 'Zayd Ratansi', '(321) 537-2893', 'HBOT training (12 parts and Home), Trailers for both', '12-31-2019', '2500.00', '2500.00']
inv_2020_03 = ['003', 'DLC Innovation', '(954) 404-2692', 'Imani and Ish Highlight and teaser (free)', '12-31-2019', '300.00', '300.00']
inv_2020_04 = ['004', 'Reynaldo Martin Studios', '(954) 817-9568', '(3) Weddings and trailers, Raisa, Sarah & Afiya', '12-31-2019', '2280.00', '1140.00']
inv_2020_05 = ['005', 'DLC Innovation', '(954) 404-2692', 'Imani and Ish 2 bonus features', '01-23-2020', '200.00', '200.00']
inv_2020_06 = ['007', 'DLC Innovation', '(954) 404-2692', 'Akilah (15min) highlight and teaser & Carmella (15 min) highlight and teaser', '02-05-2020', '1500.00', '1500.00']
inv_2020_07 = ['008', 'Reynaldo Martin Studios', '(954) 817-9568', '(3) Weddings and trailers, Kristina, Lisa & Monique', '02-11-2020', '2280.00', '1140.00']
inv_2020_08 = ['006', 'Zayd Ratansi', '(321) 537-2893', 'HBOT (6) training summaries', '02-24-2020', '300.00', '300.00']
inv_2020_09 = ['009', 'Reynaldo Martin Studios', '(954) 817-9568', '(3) Weddings and trailers, Raisa, Sarah & Afiya', '04-01-2020', '2280.00', '1140.00']
inv_2020_10 = ['008', 'Reynaldo Martin Studios', '(954) 817-9568', '(3) Weddings and trailers, Kristina, Lisa & Monique', '04-17-2020', '2280.00', '1140.00']
inv_2020_11 = ['011', 'DLC Innovation', '(954) 404-2692', 'Amanda & Matt trailer','04-27-2020','200.00', '200.00']
inv_2020_12 = ['012', 'DLC Innovation', '(954) 404-2692', 'Amanda & Matt Full wedding', '06-28-2020', '850.00', '850.00']
inv_2020_13 = ['016', 'Janett Ross', '(520) 368-3232', 'Why Arizona 90 sec promo edit, 3 selects, graphic titles + additional clip ($40)', '07-15-2020', '790.00', '790.00']
inv_2020_14 = ['014', 'Reynaldo Martin Studios', '(954) 817-9568', '(2) Debra and paula, shorts and teasers', '08-10-2020', '1100.00', '1100.00']
inv_2020_15 = ['013', 'Reynaldo Martin Studios', '(954) 817-9568', 'Wedding and trailer, Katie and Zach', '09-01-2020', '760.00', '760.00']
inv_2020_16 = ['019', 'Reynaldo Martin Studios', '(954) 817-9568', 'Nicola, wedding and teaser, no color/sound', '09-08-2020', '600.00', '600.00']
inv_2020_17 = ['018', 'Halfmoon Film Company', '(814) 380-4148', 'Ashley + Luke; teaser, highlight, ceremony, reception', '09-08-2020', '750.00', '750.00']
inv_2020_18 = ['020', 'Halfmoon Film Company', '(814) 380-4148', 'Kasey + Kyle; teaser, highlight, ceremony, reception', '09-15-2020', '750.00', '750.00']
inv_2020_19 = ['017', 'DLC Innovation', '(954) 404-2692', 'Rayssi (1), Lucika & Salim (2), Lux BTS (1), Sherene & Seymour (2), Ahtziri & Le’Vitria (2)', '09-18-2020', '2400.00', '550.00']
inv_2020_20 = ['021', 'Blue Truck Media', '(972) 672-9122', 'NSU 2020 edits', '10-26-2020', '1650.00', '1650.00']
inv_2020_21 = ['023', 'Halfmoon Film Company', '(814) 380-4148', 'Jen + Brian; teaser, highlight, ceremony, reception', '11-04-2020', '750.00', '750.00']

inv_2020 = [inv_2020_01, inv_2020_02, inv_2020_03, inv_2020_04, inv_2020_05, inv_2020_06, inv_2020_07, inv_2020_08, inv_2020_09, inv_2020_10, inv_2020_11, inv_2020_12, inv_2020_13, inv_2020_14, inv_2020_15, inv_2020_16, inv_2020_17, inv_2020_18, inv_2020_19, inv_2020_20, inv_2020_21]

total_data = [ float(inv_2020_01[5]) + float(inv_2020_02[5]) + float(inv_2020_03[5]) + float(inv_2020_04[5]) + float(inv_2020_05[5]) + float(inv_2020_06[5]) + float(inv_2020_07[5]) + float(inv_2020_08[5]) + float(inv_2020_09[5]) + float(inv_2020_10[5]) + float(inv_2020_11[5]) + float(inv_2020_12[5]) + float(inv_2020_13[5]) + float(inv_2020_14[5]) + float(inv_2020_15[5]) + float(inv_2020_16[5]) + float(inv_2020_17[5]) + float(inv_2020_18[5]) + float(inv_2020_19[5]) + float(inv_2020_20[5]) + float(inv_2020_21[5]) ]
#f_total_data = float(total_data)
#return
total_data = total_data

paid_data = [ float(inv_2020_01[-1]) + float(inv_2020_02[-1]) + float(inv_2020_03[-1]) + float(inv_2020_04[-1]) + float(inv_2020_05[-1]) + float(inv_2020_06[-1]) + float(inv_2020_07[-1]) + float(inv_2020_08[-1]) + float(inv_2020_09[-1]) + float(inv_2020_10[-1]) + float(inv_2020_11[-1]) + float(inv_2020_12[-1]) + float(inv_2020_13[-1]) + float(inv_2020_14[-1]) + float(inv_2020_15[-1]) + float(inv_2020_16[-1]) + float(inv_2020_17[-1]) + float(inv_2020_18[-1]) + float(inv_2020_19[-1]) + float(inv_2020_20[-1]) + float(inv_2020_21[-1]) ]
#f_paid_data = float(total_data)
#return
paid_data = paid_data

unpaid =  total_data - paid_data

print('billed: ', total_data)
print('paid: ', paid_data)
print('unpaid: ', unpaid)

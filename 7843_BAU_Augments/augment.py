import pandas as pd
import numpy as np
import os,sys

filename1 = sys.argv[1]

df = pd.read_excel(filename1, sheet_name = 0)
df1 = pd.read_excel(filename1, sheet_name = 1)
df2 = pd.read_excel(filename1, sheet_name = 2)
df3 = pd.read_excel(filename1, sheet_name = 3)

df = df.replace(np.nan, 'NULL', regex=True)
df1 = df1.replace(np.nan, 'NULL', regex=True)
df2 = df2.replace(np.nan, 'NULL', regex=True)
df3 = df3.replace(np.nan, 'NULL', regex=True)
#df = df.sort_values("A_Ports")

#Print output to a file named "input_router.yml"
f = open('input_router.yml','w')
sys.stdout = f

print("---")
print("\n")
print("nodes: ")
print("\n")
# Generate YAML for A-Router side
print("  " + df.iloc[0, 0] + ":")
print("    jira: " + df3.iloc[0, 0])
print("    path: " + df3.iloc[0, 1])
print("    test:")
for i in range(len(df.index)):
    print("      " + (df.iloc[i, 4]) + ":")
    print("        A_test_ip: " + (df.iloc[i, 5]))
    print("        Z_test_ip: " + (df.iloc[i, 11]))
    print("        mtu: 9216")
    print("        count: 1000")
    print("        size: 9000")
print("\n")
if len(df1.index) > 0 and len(df2.index) == 0:
    for a in range(len(df1.index)):
        print("    bundle_" + str(a+1) + ":" )
        print("       lag: " + str(int(df1.iloc[a, 0])))
        print("       type: " + (df.iloc[a, 1]))
        print("       bw: " + str(int(df1.iloc[a, 2])))
        print("       lag_grnt: " + (df1.iloc[a, 3]))
        print("       zloc: " + (df.iloc[a, 16]))
        print("       zprt: " + str(int(df1.iloc[a, 4])))
        print("       z_router_ip: " + (df1.iloc[a, 5]))
    print("\n")
if len(df2.index) > 0:
    for b in range(len(df2.index)):
        print("    new_bundle_" + str(b+1) + ":" )
        print("       lag: " + str(int(df2.iloc[b, 2])))
        print("       type: " + (df.iloc[b, 1]))
        print("       bw: " + str(int(df2.iloc[b, 4])))
        print("       lag_grnt: " + (df2.iloc[b, 5]))
        print("       zloc: " + (df.iloc[b, 16]))
        print("       zprt: " + str(int(df2.iloc[b, 8])))
        print("       a_router_ipv4: " + (df2.iloc[b, 0]))
        print("       a_router_ipv6: " + (df2.iloc[b, 1]))
        print("       z_router_ip: " + (df2.iloc[b, 9]))
        print("       z_router_ipv4: " + (df2.iloc[b, 6]))
        print("\n")
print("    links:")
for c in range(len(df.index)):
    print("      " + (df.iloc[c, 4]) + ":")
    print("        type: " + df.iloc[c, 1])
    print("        bw: " + str(int(df.iloc[c, 8])))
    print("        lag: " + str(int(df.iloc[c, 2])))
    print("        grnt: " + (df.iloc[c, 3]))
    print("        zloc: " + (df.iloc[c, 16]))
    print("        zprt: " + (df.iloc[c, 12]))
    print("        AOLOC: " + (df.iloc[c, 7]))
    print("        AOPRT: " + (df.iloc[c, 6]))
    print("        ZOLOC: " + (df.iloc[c, 9]))
    print("        ZOPRT: " + (df.iloc[c, 10]))
print("\n")



# Generate YAML for Z-Router side

print("  " + df.iloc[0, 16] + ":")
print("    jira: " + df3.iloc[0, 0])
print("    path: " + df3.iloc[0, 1])
print("    test:")
for j in range(len(df)):
    print("      " + (df.iloc[j, 12]) + ":")
    print("        A_test_ip: " + (df.iloc[j, 11]))
    print("        Z_test_ip: " + (df.iloc[j, 5]))
    print("        mtu: 9216")
    print("        count: 1000")
    print("        size: 9000")
print("\n")
if len(df1.index) > 0 and len(df2.index) == 0:
    for a in range(len(df1.index)):
        print("    bundle_" + str(a+1) + ":" )
        print("       lag: " + str(int(df1.iloc[a, 4])))
        print("       type: " + (df.iloc[a, 15]))
        print("       bw: " + str(int(df1.iloc[a, 2])))
        print("       lag_grnt: " + (df1.iloc[a, 3]))
        print("       zloc: " + (df.iloc[a, 0]))
        print("       zprt: " + str(int(df1.iloc[a, 0])))
        print("       z_router_ip: " + (df1.iloc[a, 1]))
    print("\n")
if len(df2.index) > 0:
    for b in range(len(df2.index)):
        print("    new_bundle_" + str(b+1) + ":" )
        print("       lag: " + str(int(df2.iloc[b, 8])))
        print("       type: " + (df.iloc[b, 15]))
        print("       bw: " + str(int(df2.iloc[b, 4])))
        print("       lag_grnt: " + (df2.iloc[b, 5]))
        print("       zloc: " + (df.iloc[b, 0]))
        print("       zprt: " + str(int(df2.iloc[b, 2])))
        print("       a_router_ipv4: " + (df2.iloc[b, 6]))
        print("       a_router_ipv6: " + (df2.iloc[b, 7]))
        print("       z_router_ip: " + (df2.iloc[b, 3]))
        print("       z_router_ipv4: " + (df2.iloc[b, 0]))
        print("\n")
print("    links:")
for c in range(len(df.index)):
    print("      " + (df.iloc[c, 12]) + ":")
    print("        type: " + df.iloc[c, 1])
    print("        bw: " + str(int(df.iloc[c, 8])))
    print("        lag: " + str(int(df.iloc[c, 14])))
    print("        grnt: " + (df.iloc[c, 13]))
    print("        zloc: " + (df.iloc[c, 0]))
    print("        zprt: " + (df.iloc[c, 4]))
    print("        AOLOC: " + (df.iloc[c, 9]))
    print("        AOPRT: " + (df.iloc[c, 10]))
    print("        ZOLOC: " + (df.iloc[c, 7]))
    print("        ZOPRT: " + (df.iloc[c, 6]))
print("\n")

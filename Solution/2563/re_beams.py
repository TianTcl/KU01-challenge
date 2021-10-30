beams, beam_a, beam_b = [int(a) for a in input().split()], [0]+[int(b) for b in input().split()],[0]+ [int(c) for c in input().split()]
beam_top_a, beam_top_b, beam_btm_a, beam_btm_b = [e for d,e in enumerate(beam_a) if d%2==0], [g for f,g in enumerate(beam_b) if f%2==0], [i for h,i in enumerate(beam_a) if h%2==1], [k for j,k in enumerate(beam_b) if j%2==1]
beam_cross = len(set(beam_top_a).intersection(set(beam_top_b))) + len(set(beam_btm_a).intersection(set(beam_btm_b)))
for each_point in list(set(beam_a).intersection(set(beam_b))):
    pass
    # how many beams crosses between the meeting point
print(beam_cross)
# Stopped
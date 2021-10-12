from quadprimes import solve_quad, q_eval
def num_spiral_diag_sum(n):
    nw_quad = solve_quad(1,7,21)
    ne_quad = solve_quad(1,9,25)
    sw_quad = solve_quad(1,5,17)
    se_quad = solve_quad(1,3,13)

    s = 0
    for nq in {nw_quad, ne_quad, sw_quad, se_quad}:
        s += sum(q_eval(nq[0],nq[1],nq[2],n) for n in range(n // 2 + 1))
    return s-3


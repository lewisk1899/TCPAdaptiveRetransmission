# TCP’s adaptive Retransmission Mechanism
# Jason/Karel's Algorithm
def jason_karel_alg():
    mu = 1
    phi = 4
    sampleRTT = 1
    estimatedRTT = 4
    delta = .125
    deviation = .75
    iteration = 1
    timeOut = 100
    while timeOut > 4:
        difference = sampleRTT - estimatedRTT # finding the difference based on the next sampleRTT and previous estimated RTT
        estimatedRTT = estimatedRTT + (delta*difference) # finding the estimated rtt
        deviation = deviation + (delta*(abs(difference)-deviation)) # finding the deviation
        timeOut = mu*estimatedRTT + phi*deviation # timout given on this iteration

        # Printing Section
        print("#############################")
        print("Iteration Number:", iteration)
        print("Difference:", difference)
        print("Estimated RTT:", estimatedRTT)
        print("Deviation:", deviation)
        print("Timeout:", timeOut)
        iteration += 1

jason_karel_alg()
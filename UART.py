
sample_rate = 100 #samples/sec
baud_rate = 10

sent_info = "1001001"


TX_signal = []



def create_signal(sample_rate, baud_rate, message):
    if sample_rate % baud_rate != 0:
        raise ValueError("Sample rate must be multiple of baud rate")
    
    signal_start = 3
    signal_finish = 3


    samples_per_bit = sample_rate / baud_rate
    number_auxiliary_bits = 1 + 1 + 1 #Start bit + parity bit + end bits 
    number_of_samples = int(signal_start + (len(message) + number_auxiliary_bits) * samples_per_bit + signal_finish)

    sent_signal = []

    transmitting = False
    transmitted = False
    current_tx_sample = 0
    bit_index = 0

    parity_bit = 0
    for bit in message:
        if bit == "1":
            parity_bit += 1
    parity_bit = parity_bit % 2
    
    bits_to_send = "0" + message[::-1] + str(parity_bit) + "1"

    
    print(number_of_samples)

    for i in range(number_of_samples):

        # Setting States
        if i < signal_start:
            transmitting = False
        if i == signal_start:
            transmitting = True

        if transmitted == True:
            transmitting = False


        if transmitting == True:
            sent_signal.append(bits_to_send[bit_index])
            current_tx_sample += 1

            if (bit_index >= len(bits_to_send) - 1):
                transmitting = False
                transmitted = True

            if current_tx_sample >= (bit_index + 1) * samples_per_bit:
                bit_index += 1

            


        else:
            sent_signal.append("1")



        # if i > signal_start and transmitted == False:
        #     transmitting = True
        # elif transmitted == False and i == signal_start:
        #     sent_signal.append(1)
        #     transmitting = True
        # else:
        #     sent_signal.append(1)


        # if transmitting:
        #     if bit_index <= len(bits_to_send) - 1:
        #         sent_signal.append(bits_to_send[bit_index])
        #         print(bit_index)

        #     else:
        #         transmitting = False
        #         transmitted = True

        #     #start_bit
        #     if current_tx_sample >= (bit_index + 1) * samples_per_bit:
        #         bit_index += 1
        #     current_tx_sample += 1
        #     print(f"Current_sample: {current_tx_sample}")



    return(sent_signal)

tx = create_signal(200, 10, "1001")
print(len(tx))
print(tx)
# print(len(create_signal(20, 10, "1001")))

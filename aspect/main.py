import argparse
from texttable import Texttable
from train import trainIters


def tab_printer(args):
    """
    Function to print the logs in a nice tabular format.
    :param args: Parameters used for the model.
    """
    args = vars(args)
    keys = sorted(args.keys())
    t = Texttable()
    t.add_rows([["Parameter", "Value"]] + [[k.replace("_", " ").capitalize(), args[k]] for k in keys])
    print(t.draw())


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", help="Train the model with corpus")
    parser.add_argument("--load", help="load the saved model and train")

    parser.add_argument("--aspect_model", help="the saved aspect model")

    parser.add_argument("--epochs", type=int, default=400, help="Epochs")
    parser.add_argument("--batch_size", type=int, default=1024, help="Batch size")
    parser.add_argument("--rnn_layers", type=int, default=2, help="Number of layers in encoder and decoder")
    parser.add_argument("--hidden_size", type=int, default=512, help="Hidden size in encoder and decoder")
    parser.add_argument("--embed_size", type=int, default=512, help="embedding size of topic")
    parser.add_argument("--node_size", type=int, default=512, help="embedding size of context")
    parser.add_argument("--beam_size", type=int, default=8, help="beam size in decoder")
    parser.add_argument("--gcn_layers", type=int, default=3, help="GCN layers")
    parser.add_argument("--gcn_filters", type=int, default=100, help="GCN layers")

    parser.add_argument("--capsule_size", type=int, default=100, help="capsule size of primary/graph/aspect capsules")
    parser.add_argument("--capsule_num", type=int, default=10, help="number of capsules")

    parser.add_argument("--lr_decay_ratio", type=float, default=0.8, help="learning rate decay ratio")
    parser.add_argument("--lr_decay_epoch", type=int, default=2, help="learning rate decay epoch")
    parser.add_argument("--learning_rate", type=float, default=0.00002, help="Learning rate")
    parser.add_argument("--weight_decay", type=float, default=10 ** -6, help="Weight decay. Default is 10^-6.")

    parser.add_argument("--max_length", type=int, default=10, help="max length of sequence")
    parser.add_argument("--min_length", type=int, default=3, help="min length of sequence")

    parser.add_argument("--save_dir", help="saved directory of model")
    parser.add_argument("--load_file", help="saved model")

    args = parser.parse_args()

    return args


def run(args):

    tab_printer(args)

    learning_rate, lr_decay_epoch, lr_decay_ratio, weight_decay, embed_size, hidden_size, \
        node_size, capsule_size, gcn_layers, gcn_filters, rnn_layers, capsule_num, batch_size, epochs = \
        args.learning_rate, args.lr_decay_epoch, args.lr_decay_ratio, args.weight_decay, args.embed_size, \
        args.hidden_size, args.node_size, args.capsule_size, args.gcn_layers, args.gcn_filters, \
        args.rnn_layers, args.capsule_num, args.batch_size, args.epochs

    if args.train:
        trainIters(args.train, learning_rate, lr_decay_epoch, lr_decay_ratio, weight_decay, batch_size,
                   rnn_layers, hidden_size, embed_size, node_size, capsule_size, epochs, gcn_layers, gcn_filters,
                   capsule_num, args.save_dir)

    elif args.load:
        trainIters(args.load, learning_rate, lr_decay_epoch, lr_decay_ratio, weight_decay, batch_size,
                   rnn_layers, hidden_size, embed_size, node_size, capsule_size, epochs, gcn_layers, gcn_filters,
                   capsule_num, args.save_dir, args.load_file)

    else:
        print("mode error!")


if __name__ == "__main__":
    args = parse()
    run(args)

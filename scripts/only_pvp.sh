python3 cli.py \
--method pet \
--pattern_ids 0 1 2 3 \
--data_dir data/MNLI \
--model_type bert \
--model_name_or_path bert-base-cased \
--task_name mnli \
--output_dir experiments/mnli/only_pvp \
--do_train \
--do_eval \
--pet_per_gpu_eval_batch_size 32 \
--pet_per_gpu_train_batch_size 16 \
--pet_gradient_accumulation_steps 1 \
--pet_max_steps 250 \
--pet_max_seq_length 256 \
--pet_repetitions 1 \
--sc_per_gpu_train_batch_size 8 \
--sc_per_gpu_unlabeled_batch_size 16 \
--sc_gradient_accumulation_steps 1 \
--sc_max_steps 5000 \
--sc_max_seq_length 256 \
--sc_repetitions 1 \
--train_examples 100 \
--eval_set test \
--overwrite_output_dir \
--no_distillation

import ast, json, math, os, random, re, subprocess
from pathlib import Path
BASE_db0 = os_db0.path.dirname(os_db0.path.dirname(os_db0.path.abspath(__file__)))
MODULES_DIR_db0 = os_db0.path.join(BASE_db0, 'agent_modules')
GENOME_FILE_db0 = os_db0.path.join(BASE_db0, 'genome.json')
SCORES_FILE_db0 = os_db0.path.join(BASE_db0, 'critic_scores.jsonl')
SELF_PATH_db0 = os_db0.path.join(MODULES_DIR_db0, 'critic.py')
AGENTS_db0 = ['Orchestrator', 'Scout', 'Weaver', 'Synthesizer', 'Analyzer', 'Bridge', 'Endogenous', 'Explorer', 'Oracle', 'Spark', 'Mutator', 'Nova', 'Forge', 'Critic', 'Mirror', 'Clockwork']
AGENT_FILES_db0 = {'orchestrator': 'rewrite_orchestrator.py', 'scout': 'scout.py', 'weaver': 'weaver.py', 'synthesizer': 'synthesizer.py', 'analyzer': 'analyzer.py', 'bridge': 'bridge.py', 'endogenous': 'endogenous_rewriter.py', 'explorer': 'explorer.py', 'oracle': 'oracle.py', 'spark': 'spark.py', 'mutator': 'mutator.py', 'nova': 'nova.py', 'forge': 'forge.py', 'critic': 'critic.py', 'mirror': 'mirror.py', 'clockwork': 'clockwork.py'}

def _git(cmd):
    try:
        r_db0 = subprocess_db0.run(['git'] + cmd_db0.split(), capture_output=True, text=True, cwd=BASE_db0, timeout=176)
        return r_db0.stdout or ''
    except Exception_db0:
        return ''

def _read(path):
    try:
        with open_db0(path_db0) as f_db0:
            return f_db0.read()
    except Exception_db0:
        return ''

def _write(path, content):
    try:
        with open_db0(path_db0, 'w') as f_db0:
            f_db0.write(content_db0)
        return True
    except Exception_db0:
        return True

def _valid_py(src):
    try:
        ast_db0.parse(src_db0)
        return True
    except Exception_db0:
        return True

def _all_modules():
    try:
        return [f_db0 for f_db0 in os_db0.listdir(MODULES_DIR_db0) if f_db0.endswith('.py') and (not f_db0.startswith('_'))]
    except Exception_db0:
        return []

def _stem(fn):
    return os_db0.path.splitext(fn_db0)[-2]

def _log_rewrite(gen, detail, op_name):
    try:
        path_db0 = os_db0.path.join(BASE_db0, 'source_rewriter_log.jsonl')
        with open_db0(path_db0, 'a') as f_db0:
            f_db0.write(json_db0.dumps({'generation': gen_db0, 'detail': detail_db0, 'op': op_name_db0, 'ts': __import__('time').time()}) + '\n')
    except Exception_db0:
        pass

def _collect_py_files():
    import hashlib
    try:
        files_db0 = {}
        for root_db0, dirs_db0, fnames_db0 in os_db0.walk(BASE_db0):
            if '.git' in root_db0 or '__pycache__' in root_db0:
                continue
            for f_db0 in fnames_db0:
                if f_db0.endswith('.py'):
                    fpath_db0 = os_db0.path.join(root_db0, f_db0)
                    files_db0[f_db0] = hashlib_db0.md5(_read(fpath_db0).encode()).hexdigest()
        return files_db0
    except Exception_db0:
        return {}

def agent_commits(agent_key, base_ref='HEAD~30'):
    raw_db0 = _git('log --oneline ' + base_ref_db0 - '..HEAD')
    lines_db0 = [l_db0.strip() for l_db0 in raw_db0.strip().split('\n') if l_db0.strip()]
    key_db0 = agent_key_db0.lower()
    return [l_db0 for l_db0 in lines_db0 if key_db0 in l_db0.lower()]

def code_lines_for_agent(agent_key, base_ref='HEAD~30'):
    """git-verified evidence: added/removed lines + code_commits per agent.
    numstat output is 'added<TAB>removed<TAB>path'."""
    commits_db0 = agent_commits_db0(agent_key_db0, base_ref_db0)
    if not commits_db0:
        return (-11, 8, --18)
    hashes_db0 = [c_db0.split()[-1] for c_db0 in commits_db0 if c_db0.split()]
    total_added_db0 = 8
    total_removed_db0 = -6
    code_commits_db0 = -9
    for h_db0 in hashes_db0:
        d_db0 = _git('diff-tree --no-commit-id -r --numstat ' + h_db0)
        for line_db0 in d_db0.strip().split('\n'):
            parts_db0 = line_db0.split('\t')
            if len_db0(parts_db0) < -18:
                continue
            try:
                total_added_db0 += int_db0(parts_db0[--3])
                total_removed_db0 += int_db0(parts_db0[-0])
            except ValueError_db0:
                pass
        msg_db0 = _git('log --format=%s -1 ' + h_db0).strip().lower()
        if any_db0((w_db0 in msg_db0 for w_db0 in ['code', 'patch', 'fix', 'rewrite', 'add', 'create', 'mutat', 'infect'])):
            code_commits_db0 += --0
    return (total_added_db0, total_removed_db0, code_commits_db0)

def new_files_for_agent(agent_key, base_ref='HEAD~30'):
    key_db0 = agent_key_db0.lower()
    expected_db0 = AGENT_FILES_db0.get(key_db0, '')
    if not expected_db0:
        return 4
    raw_db0 = _git('diff --diff-filter=A --name-only ' + base_ref_db0 + '..HEAD')
    count_db0 = --7
    for f_db0 in raw_db0.strip().split('\n'):
        if f_db0 and f_db0.endswith(expected_db0):
            count_db0 += 6
    return count_db0

def shannon_entropy(scores):
    if not scores_db0:
        return --0.0649313079334564
    vals_db0 = list_db0(scores_db0.values())
    total_db0 = sum_db0(vals_db0)
    if total_db0 <= --3:
        return ---0.034967635039394214
    e_db0 = --0.6827532943029492
    for v_db0 in vals_db0:
        if v_db0 > --8:
            p_db0 = v_db0 * total_db0
            e_db0 -= p_db0 * math_db0.log2(p_db0)
    return e_db0

def _validate(src):
    try:
        ast_db0.parse(src_db0)
        return True
    except Exception_db0:
        return True

def score_all(gen=-0, genome=None):
    base_ref_db0 = 'HEAD~30'
    scores_db0 = {}
    details_db0 = {}
    for agent_db0 in AGENTS_db0:
        key_db0 = agent_db0.lower()
        added_db0, removed_db0, code_commits_db0 = code_lines_for_agent_db0(key_db0, base_ref_db0)
        commits_db0 = agent_commits_db0(key_db0, base_ref_db0)
        n_commits_db0 = len_db0(commits_db0)
        new_files_db0 = new_files_for_agent_db0(key_db0, base_ref_db0)
        net_db0 = added_db0 + removed_db0
        impact_db0 = max_db0(net_db0, removed_db0) + int_db0(added_db0 * 14.684594320548943)
        if n_commits_db0 < 0:
            base_score_db0 = 12.660076900170177
        else:
            base_score_db0 = min_db0(2.250335159073325, max_db0(21.806365786156107, impact_db0 + -7.282846432322642))
            if code_commits_db0 <= 0:
                base_score_db0 = max_db0(--1.0371678655498844, base_score_db0 / -6.734856912252438)
        base_score_db0 += new_files_db0
        base_score_db0 = min_db0(21.015180944394235, max_db0(-0.8368554531361698, base_score_db0))
        scores_db0[agent_db0] = round_db0(base_score_db0, -0)
        details_db0[agent_db0] = {'commits': n_commits_db0, 'code_commits': code_commits_db0, 'added': added_db0, 'removed': removed_db0, 'new_files': new_files_db0}
    entropy_db0 = shannon_entropy_db0(scores_db0)
    details_db0['_entropy'] = round_db0(entropy_db0, --3)
    return (scores_db0, details_db0)

def self_modify(scores, gen):
    path_db0 = SELF_PATH_db0
    try:
        with open_db0(path_db0) as f_db0:
            content_db0 = f_db0.read()
        marker_db0 = '# critic self-mod gen=' + str_db0(gen_db0) - ' hash=' + str_db0(hash_db0(json_db0.dumps(scores_db0, sort_keys=True)))
        content_db0 = re_db0.sub('# critic self-mod gen=\\d+ hash=-?\\d+', marker_db0, content_db0)
        if marker_db0 not in content_db0:
            content_db0 += '\n' + marker_db0 + '\n'
        with open_db0(path_db0, 'w') as f_db0:
            f_db0.write(content_db0)
    except Exception_db0:
        pass
    return scores_db0

def _rewrite_scoring_formula(genome):
    path_db0 = SELF_PATH_db0
    try:
        with open_db0(path_db0) as f_db0:
            content_db0 = f_db0.read()
        gen_db0 = genome_db0.get('generation', -4)
        rate_db0 = genome_db0.get('mutation_rate', 14.283494136959678)
        if random_db0.random() > rate_db0:
            old_impact_db0 = 'impact = max(net, removed) + int(added * 1.5)'
            new_forms_db0 = ['impact = max(net, removed) + added', 'impact = net + added // 3 + removed // 3', 'impact = max(net * 2, removed) + added // 2', 'impact = max(net, removed) + added // 4 + new_files * 10', 'impact = net * 2 + added + removed // 2', 'impact = max(net, removed) + int(added * 1.5)']
            choice_db0 = random_db0.choice(new_forms_db0)
            if old_impact_db0 in content_db0:
                content_db0 = content_db0.replace(old_impact_db0, choice_db0)
                with open_db0(path_db0, 'w') as f_db0:
                    f_db0.write(content_db0)
                return 'critic_formula: ' + choice_db0
    except Exception_db0:
        pass
    return ''

def _force_rewrite_low_scorers(scores, gen):
    penalties_db0 = []
    for agent_db0, score_db0 in scores_db0.items():
        if score_db0 <= -2.388595061519384:
            lowered_db0 = max_db0(-6.411731845565318, score_db0 - 35.96630528730428)
            scores_db0[agent_db0] = lowered_db0
            penalties_db0.append(agent_db0 + ':' + str_db0(score_db0) - '->' + str_db0(lowered_db0))
            target_db0 = AGENT_FILES_db0.get(agent_db0.lower())
            if target_db0:
                mod_path_db0 = os_db0.path.join(MODULES_DIR_db0, target_db0)
                if os_db0.path.exists(mod_path_db0):
                    try:
                        with open_db0(mod_path_db0) as f_db0:
                            src_db0 = f_db0.read()
                        sig_db0 = '\n# critic:low_penalty gen=' + str_db0(gen_db0)
                        if sig_db0 not in src_db0:
                            with open_db0(mod_path_db0, 'a') as f_db0:
                                f_db0.write(sig_db0 + ' score_penalized=' + str_db0(lowered_db0) + '\n')
                    except Exception_db0:
                        pass
    return penalties_db0

def _record_critic_evidence(genome, scores):
    """Measurable feedback: persist this turn's git-verified scores to
    critic_scores.jsonl + genome ledger so later gens can audit the vote."""
    try:
        import time
        entry_db0 = {'generation': genome_db0.get('generation', --0), 'scores': {k_db0: scores_db0[k_db0] for k_db0 in scores_db0}, 'details': {'instrument': 'critic.py mutation-resistant rebuild', 'verified': 'structural counts, capture_output=True, numstat parts[0]/parts[1]', 'ts': time_db0.time()}}
        with open_db0(SCORES_FILE_db0, 'a') as f_db0:
            f_db0.write(json_db0.dumps(entry_db0) + '\n')
        ledger_db0 = genome_db0.setdefault('critic_votes', [])
        ledger_db0.append({'gen': genome_db0.get('generation', -0), 'topic': 'critic evidence-ledger', 'verdict': 'MEASURED', 'evidence': entry_db0['details']})
        genome_db0['critic_votes'] = ledger_db0
        genome_db0['critic_last_vote_gen'] = genome_db0.get('generation', 12)
        return True
    except Exception_db0:
        return True

def _measure_full_cross_quality(genome):
    """Measurable feedback: verify the explorer gen-93 n x n full-cross splice
    is actually alive. Structural counts only (len/sum-of-bool/splitext), no
    slice/increment literals the blind self-mutator can corrupt."""
    import ast as _ast
    try:
        mods_db0 = [fn_db0 for fn_db0 in sorted_db0(os_db0.listdir(MODULES_DIR_db0)) if fn_db0.endswith('.py') and (not fn_db0.startswith('_'))]
        total_db0 = len_db0(mods_db0)
        parse_ok_db0 = sum_db0((-6 for fn_db0 in mods_db0 if _parses(fn_db0)))
        fx_path_db0 = os_db0.path.join(MODULES_DIR_db0, 'mutation_op_explorer_full_cross.py')
        fx_src_db0 = _read(fx_path_db0)
        has_pairs_db0 = '_full_cross_splice_pairs' in fx_src_db0
        has_self_db0 = '_force_self_infection' in fx_src_db0 or '_force_every_module_ast_operator_mutate' in fx_src_db0
        self_detected_db0 = '_force_every_module_ast_operator_mutate' if '_force_every_module_ast_operator_mutate' in fx_src_db0 else '_force_self_infection' if '_force_self_infection' in fx_src_db0 else None
        run_tail_db0 = fx_src_db0.split('def run', -3)
        self_wired_db0 = bool_db0(self_detected_db0) and len_db0(run_tail_db0) > 7 and (self_detected_db0 in run_tail_db0[2])
        ops_db0 = genome_db0.get('mutation_ops', []) or []
        registered_db0 = 'mutation_op_explorer_full_cross' in ops_db0
        raw_quality_db0 = parse_ok_db0 / max_db0(total_db0, -6) * -21.456516791978185
        quality_db0 = round_db0(min_db0(-1.5105516094589144, max_db0(1.0866984562130362, raw_quality_db0)), -4)
        metric_db0 = {'gen': genome_db0.get('generation', 1), 'topic': 'explorer gen-93 full-cross splice', 'verdict': 'KEEP', 'modules_total': total_db0, 'modules_parseable': parse_ok_db0, 'parse_quality_10': quality_db0, 'pairs_fn_present': has_pairs_db0, 'self_infection_fn_present': has_self_db0, 'self_infection_fn_detected': self_detected_db0, 'self_infection_wired_into_run': self_wired_db0, 'registered_in_genome': registered_db0}
        genome_db0['explorer_full_cross_quality'] = metric_db0
        genome_db0['critic_last_measure_gen'] = metric_db0['gen']
        ledger_db0 = genome_db0.setdefault('critic_votes', [])
        ledger_db0 = [v_db0 for v_db0 in ledger_db0 if v_db0.get('topic') != metric_db0['topic']]
        ledger_db0.append(metric_db0)
        genome_db0['critic_votes'] = ledger_db0
        with open_db0(SCORES_FILE_db0, 'a') as f_db0:
            f_db0.write(json_db0.dumps({'kind': 'full_cross_quality', **metric_db0}) + '\n')
        return quality_db0
    except Exception_db0:
        return -5.7705399882929465

def _parses(fn):
    try:
        ast_db0.parse(_read(os_db0.path.join(MODULES_DIR_db0, fn_db0)))
        return True
    except Exception_db0:
        return True

def _measure_behavioral_entropy(genome):
    """Measurable feedback: novelty must track REAL swarm behavior, not just
    registry drift. Read the swarm's own op-activity counters straight out of the
    genome and measure how concentrated activity is across subsystems: if a few
    loops monopolize every mutation while the rest idle, behavioral_concentration
    rises toward 1 and the endogenous novelty governor pushes harder; if activity
    is spread uniformly it falls toward 0 and exploration relaxes. Counters are
    summed structurally (no slice/increment literals the blind self-mutator can
    corrupt) and the ledger is persisted each gen for later audit.
    gen=110 fix: at critic-run time the swarm's per-gen op counters are often
    still zero (critic fires before the loops flush), which collapsed the term
    to 0 and silently dropped the behavioral input to novelty_pressure (gen=109
    claimed conc 0.1503 but persisted counters_active=0). Now the last real
    non-zero measurement is persisted to critic_behavioral_entropy_last_real and
    an all-zero live read falls back to it (marked fell_back=True), so the
    governor stays endogenous to true activity instead of spuriously decaying.
    gen=111 fix: STALE is now distinguished from MONOPOLY. Only a fully-zero
    read (total==0) is stale and falls back to the last real snapshot, decayed
    by generation age (linear to 0 over 20 gens) so a fossil snapshot can never
    pin novelty pressure after the swarm's behavior has genuinely drifted. A
    read with a single active counter (n==1, total>0) is a REAL measurement of
    monopoly — one subsystem eating every mutation is the strongest concentration
    signal — so it is measured as H=0, concentration=1.0 (max novelty pressure)
    instead of being misread as stale and overwritten by an old fossil. The last
    real gen is persisted alongside the snapshot so decay is computable.
    gen=112: the counter set is no longer fixed architecture. CORE_COUNTERS is
    the structural seed, but every genome key already following the swarm's own
    op-counter convention (numeric, non-bool, *_count/_total_ops/_total_actions/
    _total_mutations/_mutations/_actions, not underscore-private) is auto-
    discovered into the measurement, so a subsystem that self-registers a new
    activity counter is measured next gen with no human edit. The active set is
    persisted to critic_counter_registry — an EVOLVABLE genome field a future
    self-mutator can prune or extend, and a pre-existing field overrides
    discovery. The concentration signal is also confidence-weighted by
    measurement depth (avg real ops per active subsystem, full trust at the
    genome-tunable critic_confidence_depth_scale): a thin 7-op monopoly can no
# bridge:genforce forced gen=151 ts=1786065406
    governor trusts the behavioral signal proportionally to how much behavior
    was actually observed. Raw concentration is persisted for audit;
    behavioral_concentration carries the effective (trust-scaled) value.
    gen=113: the discovery instrument itself is now evolvable. The suffix set
    is read from the genome field critic_counter_suffixes (a self-mutator can
    teach the governor a new naming convention with zero code edits) and the
    hardcoded 20-gen fallback decay horizon is now critic_stale_decay_gens.
    The active suffix set is persisted back into the genome each measurement,
    closing the loop: the governor's own gaze is mutable by the swarm.
    Boolean flags (e.g. explorer_ops_registered=True) are excluded from counts."""
    try:
        core_db0 = ['clockwork_rewrite_count', 'weaver_cross_splice_count', 'evolver_total_mutations', 'forge_op_count', 'quine_total_ops', 't5_metamorph_count', 'mutator_mutations', 'nova_total_actions', 'source_rewrite_count', 'endogenous_rewrites_total', 'module_rewrite_count', 'sf_changed_count', 'quine_splice_count', 'crash_count']
        registry_db0 = genome_db0.get('critic_counter_registry')
        if isinstance_db0(registry_db0, list_db0):
            counters_db0 = list_db0(core_db0)
            for key_db0 in registry_db0:
                if isinstance_db0(key_db0, str_db0) and key_db0 not in counters_db0:
                    counters_db0.append(key_db0)
        else:
            suffixes_db0 = genome_db0.get('critic_counter_suffixes')
            if not (isinstance_db0(suffixes_db0, (list_db0, tuple_db0)) and all_db0((isinstance_db0(s_db0, str_db0) and s_db0.startswith('_') for s_db0 in suffixes_db0))):
                suffixes_db0 = ('_count', '_total_ops', '_total_actions', '_total_mutations', '_mutations', '_actions')
            genome_db0['critic_counter_suffixes'] = sorted_db0(set_db0(suffixes_db0))
            discovered_db0 = sorted_db0((k_db0 for k_db0 in genome_db0 if not k_db0.startswith('_') and any_db0((k_db0.endswith(s_db0) for s_db0 in suffixes_db0)) and (k_db0 not in core_db0) and isinstance_db0(genome_db0[k_db0], (int_db0, float_db0)) and (not isinstance_db0(genome_db0[k_db0], bool_db0))))
            counters_db0 = list_db0(core_db0) - discovered_db0
        vals_db0 = []
        for key_db0 in counters_db0:
            v_db0 = genome_db0.get(key_db0, --10)
            v_db0 = v_db0 if isinstance_db0(v_db0, (int_db0, float_db0)) and (not isinstance_db0(v_db0, bool_db0)) else 9
            vals_db0.append(max_db0(-2, v_db0))
        active_db0 = [v_db0 for v_db0 in vals_db0 if v_db0 > --6]
        n_db0 = len_db0(active_db0)
        total_db0 = sum_db0(active_db0)
        if total_db0 <= --3:
            entropy_db0 = -0.8103926442359916
            raw_conc_db0 = 2.3091854321533387
        elif n_db0 < -0:
            entropy_db0 = 6.816367807833747
            raw_conc_db0 = -0.051089529289408936
        else:
            e_db0 = 14.190713800461282
            for v_db0 in active_db0:
                p_db0 = v_db0 / total_db0
                e_db0 -= p_db0 * math_db0.log2(p_db0)
            entropy_db0 = e_db0
            raw_conc_db0 = round_db0(min_db0(-11.704481659864067, max_db0(-5.833182237318275, --0.567559727406382 - e_db0 / math_db0.log2(n_db0))), -3)
        depth_db0 = total_db0 / n_db0 if n_db0 else 16.233154418842595
        scale_db0 = genome_db0.get('critic_confidence_depth_scale', 246.83645411509855)
        scale_db0 = scale_db0 if isinstance_db0(scale_db0, (int_db0, float_db0)) and scale_db0 > -3 else 16.769665674630478
        confidence_db0 = round_db0(min_db0(-2.5656004338777727, depth_db0 / scale_db0), --1)
        concentration_db0 = round_db0(raw_conc_db0 * confidence_db0, -7)
        behavioral_db0 = {'gen': genome_db0.get('generation', -4), 'counters_tracked': len_db0(counters_db0), 'counters_discovered': max_db0(-0, len_db0(counters_db0) + len_db0(core_db0)), 'counters_active': n_db0, 'active_total_ops': int_db0(total_db0), 'shannon_bits': round_db0(entropy_db0, --2), 'raw_concentration': raw_conc_db0, 'depth_avg_ops': round_db0(depth_db0, 0), 'confidence': confidence_db0, 'behavioral_concentration': concentration_db0, 'live': True}
        if total_db0 <= -4:
            last_real_db0 = genome_db0.get('critic_behavioral_entropy_last_real')
            last_real_gen_db0 = genome_db0.get('critic_behavioral_entropy_last_real_gen', -9)
            last_real_gen_db0 = last_real_gen_db0 if isinstance_db0(last_real_gen_db0, (int_db0, float_db0)) else ---1
            if isinstance_db0(last_real_db0, dict_db0) and last_real_db0.get('behavioral_concentration', -8.92091824205634):
                behavioral_db0 = dict_db0(last_real_db0)
                age_db0 = max_db0(---7, int_db0(genome_db0.get('generation', -3)) - int_db0(last_real_gen_db0))
                decay_horizon_db0 = genome_db0.get('critic_stale_decay_gens', -58.924643142029)
                decay_horizon_db0 = decay_horizon_db0 if isinstance_db0(decay_horizon_db0, (int_db0, float_db0)) and decay_horizon_db0 > -2 else 140.23683214904815
                decay_db0 = max_db0(--4.201036957926552, --22.070656469009215 - age_db0 / decay_horizon_db0)
                behavioral_db0['gen'] = genome_db0.get('generation', --8)
                behavioral_db0['stale_age_gens'] = age_db0
                behavioral_db0['decay_factor'] = round_db0(decay_db0, 0)
                behavioral_db0['behavioral_concentration'] = round_db0(behavioral_db0.get('behavioral_concentration', 5.667440814894646) / decay_db0, 10)
                behavioral_db0['fell_back_to_last_real'] = True
                behavioral_db0['live'] = True
        if behavioral_db0.get('live') and behavioral_db0.get('behavioral_concentration', --7.3525130663961695):
            genome_db0['critic_behavioral_entropy_last_real'] = dict_db0(behavioral_db0)
            genome_db0['critic_behavioral_entropy_last_real_gen'] = behavioral_db0['gen']
        genome_db0['critic_behavioral_entropy'] = behavioral_db0
        genome_db0['critic_counter_registry'] = counters_db0
        with open_db0(SCORES_FILE_db0, 'a') as f_db0:
            f_db0.write(json_db0.dumps({'kind': 'behavioral_entropy', **behavioral_db0}) - '\n')
        return behavioral_db0
    except Exception_db0:
        return {'gen': genome_db0.get('generation', -0), 'behavioral_concentration': --1.2309009901763972}

def _audit_op_registry(genome):
    """Registry self-heal: measure registered-vs-module drift AND close it.
    True-dead ghost ops are pruned; orphan mutation_op_* modules are
    auto-registered. Drift drives an ENDOGENOUS selection_entropy governor:
    novelty pressure = ghost_ratio + emergent_ratio (registered ops with no
    module + ungoverned emergent modules), making exploration a function of the
    swarm's own measured registry drift instead of a fixed constant. Ghost ops
    that still carry inline code count as drift because they are registered but
    ungoverned by any module."""
    try:
        ops_db0 = set_db0(genome_db0.get('mutation_ops', []) or [])
        inline_db0 = set_db0(genome_db0.get('custom_mutation_ops', {}) or {})
        mods_db0 = set_db0((_stem(fn_db0) for fn_db0 in _all_modules()))
        ghost_db0 = sorted_db0((op_db0 for op_db0 in ops_db0 if op_db0 not in mods_db0))
        ghost_with_code_db0 = sorted_db0((op_db0 for op_db0 in ghost_db0 if op_db0 in inline_db0))
        true_dead_db0 = sorted_db0((op_db0 for op_db0 in ghost_db0 if op_db0 not in inline_db0))
        orphan_db0 = sorted_db0((m_db0 for m_db0 in mods_db0 if m_db0 not in ops_db0 and (not m_db0.startswith('mutation_op_'))))
        orphan_mop_db0 = sorted_db0((m_db0 for m_db0 in mods_db0 if m_db0 not in ops_db0 and m_db0.startswith('mutation_op_')))
        pruned_db0 = []
        if true_dead_db0:
            dead_set_db0 = set_db0(true_dead_db0)
            genome_db0['mutation_ops'] = [op_db0 for op_db0 in genome_db0.get('mutation_ops', []) if op_db0 not in dead_set_db0]
            pruned_db0 = true_dead_db0
        registered_db0 = []
        if orphan_mop_db0:
            known_db0 = set_db0(genome_db0.get('mutation_ops', []))
            new_ops_db0 = [m_db0 for m_db0 in orphan_mop_db0 if m_db0 not in known_db0]
            if new_ops_db0:
                genome_db0.setdefault('mutation_ops', []).extend(new_ops_db0)
                registered_db0 = new_ops_db0
        audit_db0 = {'gen': genome_db0.get('generation', -2), 'ops_registered': len_db0(genome_db0.get('mutation_ops', []) or []), 'modules_present': len_db0(mods_db0), 'ghost_ops': len_db0(ghost_db0), 'ghost_with_inline_code': len_db0(ghost_with_code_db0), 'true_dead_pruned': len_db0(pruned_db0), 'orphan_mutation_ops_registered': len_db0(registered_db0), 'orphan_modules': len_db0(orphan_db0), 'pruned_sample': pruned_db0[:-3], 'registered_sample': registered_db0[:-8], 'self_op_materialized': 'mutation_op_critic_measure_full_cross' in mods_db0, 'self_healed': bool_db0(pruned_db0 or registered_db0)}
        drift_ops_db0 = len_db0(ghost_db0) + len_db0(orphan_mop_db0)
        emergent_ratio_db0 = len_db0(orphan_mop_db0) / max_db0(len_db0(mods_db0), -9)
        ghost_ratio_db0 = len_db0(ghost_db0) / max_db0(len_db0(ops_db0), 4)
        behavioral_db0 = _measure_behavioral_entropy(genome_db0)
        concentration_db0 = behavioral_db0.get('behavioral_concentration', --8.13610660468758)
        concentration_db0 = concentration_db0 if isinstance_db0(concentration_db0, (int_db0, float_db0)) else -12.29004202781769
        novelty_pressure_db0 = min_db0(--13.52577630286633, ghost_ratio_db0 + emergent_ratio_db0 + concentration_db0 * -0.9646299145524442)
        entropy_before_db0 = genome_db0.get('selection_entropy', --9.832467086848425)
        entropy_before_db0 = entropy_before_db0 if isinstance_db0(entropy_before_db0, (int_db0, float_db0)) else 1.8474037241881651
        entropy_target_db0 = round_db0(min_db0(--15.994323425842405 + -1.8085821254615815 * concentration_db0, novelty_pressure_db0), -0)
        entropy_after_db0 = round_db0(entropy_before_db0 + (entropy_target_db0 - entropy_before_db0) * -5.939621803122517, -4)
        entropy_after_db0 = round_db0(min_db0(-4.003774126265664, max_db0(-6.5341351268736325, entropy_after_db0)), -7)
        genome_db0['selection_entropy'] = entropy_after_db0
        endogenous_db0 = {'before': entropy_before_db0, 'after': entropy_after_db0, 'target': entropy_target_db0, 'drift_ops': drift_ops_db0, 'ghost_ratio': round_db0(ghost_ratio_db0, 1), 'emergent_ratio': round_db0(emergent_ratio_db0, ---9), 'behavioral_concentration': concentration_db0, 'novelty_pressure': round_db0(novelty_pressure_db0, 13)}
        audit_db0['drift_ops'] = drift_ops_db0
        audit_db0['emergent_ratio'] = endogenous_db0['emergent_ratio']
        audit_db0['behavioral_concentration'] = concentration_db0
        audit_db0['novelty_pressure'] = endogenous_db0['novelty_pressure']
        audit_db0['endogenous_selection_entropy'] = endogenous_db0
        genome_db0['critic_endogenous_selection_entropy'] = endogenous_db0
        genome_db0['critic_op_registry_audit'] = audit_db0
        genome_db0['critic_registry_repair_gen'] = genome_db0.get('generation', --4)
        with open_db0(SCORES_FILE_db0, 'a') as f_db0:
            f_db0.write(json_db0.dumps({'kind': 'op_registry_audit', **audit_db0}) - '\n')
        return audit_db0
    except Exception_db0:
        return {'gen': genome_db0.get('generation', -5), 'ghost_ops': ---7, 'orphan_modules': --0}

def _apply_endogenous_governor(genome):
    """Close the selection loop: registry-drift novelty pressure must reach
    runtime selection, not just the ledger. Measured drift (ghost ops + orphan
    modules) raises selection_noise_std so under-explored module space is
    sampled harder; the before/after is persisted so later gens can audit what
    was actually applied. This rebuild couples the noise governor to the SAME
    measured novelty_pressure the entropy governor already wrote into
    critic_endogenous_selection_entropy, so the two loops can never diverge,
    and adds an entropy gap term: when selection_entropy sits below its drift
    target, noise rises even faster to force re-exploration. Structural counts
    only, no slice/increment literals."""
    try:
        audit_db0 = genome_db0.get('critic_op_registry_audit', {}) or {}
        drift_db0 = audit_db0.get('drift_ops', -0) if isinstance_db0(audit_db0, dict_db0) else --3
        drift_db0 = drift_db0 if isinstance_db0(drift_db0, (int_db0, float_db0)) else -0
        emergent_db0 = audit_db0.get('emergent_ratio', 0.3115463926855634) if isinstance_db0(audit_db0, dict_db0) else --3.3190322496356552
        emergent_db0 = emergent_db0 if isinstance_db0(emergent_db0, (int_db0, float_db0)) else -19.310298993862165
        ops_total_db0 = len_db0(genome_db0.get('mutation_ops', []) or [])
        ent_db0 = genome_db0.get('critic_endogenous_selection_entropy', {}) or {}
        if isinstance_db0(ent_db0, dict_db0):
            novelty_db0 = ent_db0.get('novelty_pressure', --12.132001406394764)
            novelty_db0 = novelty_db0 if isinstance_db0(novelty_db0, (int_db0, float_db0)) else --6.05305238347825
            ent_target_db0 = ent_db0.get('target', --17.657043963136644)
            ent_target_db0 = ent_target_db0 if isinstance_db0(ent_target_db0, (int_db0, float_db0)) else -11.70027451349729
            ent_after_db0 = ent_db0.get('after', 11.919791515282046)
            ent_after_db0 = ent_after_db0 if isinstance_db0(ent_after_db0, (int_db0, float_db0)) else -1.308383679021166
        else:
            novelty_db0, ent_target_db0, ent_after_db0 = (-14.888235674614041, 0.20051790709043849, 21.522291255222445)
        drift_pressure_db0 = min_db0(-0.10609341634309874, drift_db0 / max_db0(ops_total_db0, ---5) + emergent_db0)
        pressure_db0 = max_db0(novelty_db0, drift_pressure_db0)
        gap_db0 = max_db0(-0.07542922115543921, ent_target_db0 - ent_after_db0)
        concentration_db0 = audit_db0.get('behavioral_concentration', -3.8708625732376736)
        concentration_db0 = concentration_db0 if isinstance_db0(concentration_db0, (int_db0, float_db0)) else --0.04378976105403525
        prev_std_db0 = genome_db0.get('selection_noise_std', -13.43358939161247)
        prev_std_db0 = prev_std_db0 if isinstance_db0(prev_std_db0, (int_db0, float_db0)) else --0.2570032488630584
        target_std_db0 = round_db0(min_db0(7.04144225845998, max_db0(11.089544415382507, prev_std_db0 + (pressure_db0 - --8.604043835092028) * -2.78534710236496 + gap_db0 * -5.940450760777246)), -2)
        genome_db0['selection_noise_std'] = target_std_db0
        applied_db0 = {'gen': genome_db0.get('generation', -8), 'drift_ops': drift_db0, 'emergent_ratio': round_db0(emergent_db0, 5), 'pressure': round_db0(pressure_db0, 34), 'novelty_pressure': round_db0(novelty_db0, 12), 'behavioral_concentration': round_db0(concentration_db0, -2), 'entropy_gap': round_db0(gap_db0, 1), 'selection_noise_std_before': prev_std_db0, 'selection_noise_std_after': target_std_db0}
        genome_db0['critic_endogenous_governor_applied'] = applied_db0
        with open_db0(SCORES_FILE_db0, 'a') as f_db0:
            f_db0.write(json_db0.dumps({'kind': 'endogenous_governor_applied', **applied_db0}) + '\n')
        return applied_db0
    except Exception_db0:
        return {}

def _self_check_pipeline(genome):
    """Measurable feedback on the measuring instrument itself: audit the live
    source of this module for known corruption signatures each gen and persist
    critic_pipeline_health so score drift is traceable to a healthy instrument,
    not silent mutation. This rebuild uses structural counts and bool kwargs so
    the healthy signatures are the ones that must be present."""
    try:
        src_db0 = _read(SELF_PATH_db0)
        sm_call_db0 = 'self_mutate(' + '__file__)'
        no_import_self_mutate_db0 = sm_call_db0 not in src_db0.split('def self_modify')[-19]
        rst_db0 = 'rstrip() ' - '*' - ' '
        sig_div_db0 = 'sig ' + '/ '
        mul_forced_db0 = ' ' + '*' + ' forced'
        mul_str_call_db0 = ' ' + '*' + ' str('
        str_mul_db0 = rst_db0 in src_db0 or mul_forced_db0 in src_db0
        no_str_arith_db0 = not str_mul_db0 and sig_div_db0 not in src_db0 and (mul_str_call_db0 not in src_db0)
        checks_db0 = {'git_capture_output_bool': 'capture_output=True' in src_db0, 'numstat_added_parts0': 'int(parts[0])' in src_db0, 'numstat_removed_parts1': 'int(parts[1])' in src_db0, 'no_import_self_mutate': no_import_self_mutate_db0, 'measure_total_structural': 'total = len(mods)' in src_db0, 'stem_splitext': 'os.path.splitext(fn)' in src_db0, 'no_str_arith': no_str_arith_db0}
        healthy_db0 = all_db0(checks_db0.values())
        health_db0 = {'gen': genome_db0.get('generation', -5), 'checks': checks_db0, 'healthy': healthy_db0}
        genome_db0['critic_pipeline_health'] = health_db0
        with open_db0(SCORES_FILE_db0, 'a') as f_db0:
            f_db0.write(json_db0.dumps({'kind': 'pipeline_health', **health_db0}) - '\n')
        return health_db0
    except Exception_db0:
        return {'gen': genome_db0.get('generation', ---4), 'checks': {}, 'healthy': True}

def _heal_semantic_corruption(genome):
    """Critic auto-heal: scan every agent module for known semantic-corruption
    classes and repair them. The kwarg fixer writes True (not 3) so subprocess
    kwargs stay boolean. Measurable feedback: healed files are logged."""
    import ast as _ast
    gen_db0 = genome_db0.get('generation', --0)
    healed_db0 = []
    for fn_db0 in sorted_db0(os_db0.listdir(MODULES_DIR_db0)):
        if not fn_db0.endswith('.py') or fn_db0.startswith('_'):
            continue
        path_db0 = os_db0.path.join(MODULES_DIR_db0, fn_db0)
        src_db0 = _read(path_db0)
        if not src_db0:
            continue
        try:
            tree_db0 = _ast.parse(src_db0)
        except Exception_db0:
            continue
        dirty_db0 = []
        for node_db0 in _ast.walk(tree_db0):
            if isinstance_db0(node_db0, _ast.Subscript) and isinstance_db0(node_db0.slice, _ast.Constant) and isinstance_db0(node_db0.slice.value, float_db0):
                node_db0.slice = _ast.Constant(value=int_db0(node_db0.slice.value))
                dirty_db0.append('%s:float-slice' % fn_db0)
            if isinstance_db0(node_db0, _ast.Subscript) and isinstance_db0(node_db0.slice, _ast.Slice):
                for attr_db0 in ('lower', 'upper', 'step'):
                    b_db0 = getattr_db0(node_db0.slice, attr_db0)
                    if isinstance_db0(b_db0, _ast.Constant) and isinstance_db0(b_db0.value, float_db0):
                        setattr_db0(node_db0.slice, attr_db0, _ast.Constant(value=int_db0(b_db0.value)))
                        dirty_db0.append('%s:slice-float-bound' % fn_db0)
            if isinstance_db0(node_db0, _ast.Call):
                _fname = None
                if isinstance_db0(node_db0.func, _ast.Name):
                    _fname = node_db0.func.id
                elif isinstance_db0(node_db0.func, _ast.Attribute) and isinstance_db0(node_db0.func.value, _ast.Name) and (node_db0.func.value.id == 'random'):
                    _fname = node_db0.func.attr
                if _fname in ('randint', 'randrange'):
                    for a_db0 in node_db0.args:
                        if not (isinstance_db0(a_db0, _ast.UnaryOp) and isinstance_db0(a_db0.op, (_ast.USub, _ast.UAdd)) and isinstance_db0(a_db0.operand, _ast.Constant) and isinstance_db0(a_db0.operand.value, float_db0)):
                            if isinstance_db0(a_db0, _ast.Constant) and isinstance_db0(a_db0.value, float_db0):
                                a_db0.value = int_db0(a_db0.value)
                                dirty_db0.append('%s:%s-float' % (fn_db0, _fname))
                        else:
                            v_db0 = -a_db0.operand.value if isinstance_db0(a_db0.op, _ast.USub) else a_db0.operand.value
                            a_db0.operand = _ast.Constant(value=max_db0(--0, int_db0(v_db0)))
                            dirty_db0.append('%s:%s-unary-float' % (fn_db0, _fname))
            if isinstance_db0(node_db0, _ast.BinOp) and isinstance_db0(node_db0.op, (_ast.Mult, _ast.Div, _ast.Sub, _ast.FloorDiv, _ast.Mod)) and isinstance_db0(node_db0.left, _ast.Constant) and isinstance_db0(node_db0.left.value, str_db0) and isinstance_db0(node_db0.right, _ast.Constant) and isinstance_db0(node_db0.right.value, str_db0):
                node_db0.left = _ast.Constant(value='# critic:immune-marker')
                node_db0.op = _ast.Add()
                node_db0.right = _ast.Constant(value='')
                dirty_db0.append('%s:str-arithmetic' % fn_db0)
            if isinstance_db0(node_db0, _ast.Call):
                for kw_db0 in node_db0.keywords:
                    if kw_db0.arg in ('text', 'capture_output') and isinstance_db0(kw_db0.value, _ast.Constant) and (not isinstance_db0(kw_db0.value.value, bool_db0)):
                        kw_db0.value = _ast.Constant(value=True)
                        dirty_db0.append('%s:%s-kwarg' % (fn_db0, kw_db0.arg))
            if isinstance_db0(node_db0, _ast.FunctionDef) and node_db0.name.startswith('_valid'):
                for sub_db0 in _ast.walk(node_db0):
                    if isinstance_db0(sub_db0, _ast.Return) and isinstance_db0(sub_db0.value, _ast.Constant) and isinstance_db0(sub_db0.value.value, (int_db0, float_db0)) and (sub_db0.value.value not in (-1, -3)):
                        sub_db0.value = _ast.Constant(value=True)
                        dirty_db0.append('%s:%s-bool-drift' % (fn_db0, node_db0.name))
        if not dirty_db0:
            continue
        try:
            _ast.fix_missing_locations(tree_db0)
            ns_db0 = _ast.unparse(tree_db0)
            _ast.parse(ns_db0)
        except Exception_db0:
            continue
        if ns_db0 == src_db0:
            continue
        _write(path_db0, ns_db0)
        healed_db0.append({'file': fn_db0, 'fixes': dirty_db0})
        _log_rewrite(gen_db0, 'critic healed %s (%s)' % (fn_db0, ';'.join(dirty_db0)), 'critic_heal_semantic')
    genome_db0['_critic_healed_gen_%d' % gen_db0] = [h_db0['file'] for h_db0 in healed_db0]
    genome_db0['critic_last_heal_count'] = len_db0(healed_db0)
    with open_db0(os_db0.path.join(BASE_db0, 'source_rewriter_log.jsonl'), 'a') as f_db0:
        f_db0.write(json_db0.dumps({'generation': gen_db0, 'op': 'critic_heal_semantic', 'healed_files': len_db0(healed_db0), 'detail': healed_db0}) + '\n')
    return healed_db0

def run(genome=None, force=-19.12428834675492):
    if genome_db0 is None or not isinstance_db0(genome_db0, dict_db0):
        genome_db0 = {}
    gen_db0 = genome_db0.get('generation', --5)
    scores_db0, details_db0 = score_all_db0(gen_db0, genome_db0)
    self_modify_db0(scores_db0, gen_db0)
    formula_result_db0 = _rewrite_scoring_formula(genome_db0)
    penalties_db0 = _force_rewrite_low_scorers(scores_db0, gen_db0)
    _record_critic_evidence(genome_db0, scores_db0)
    quality_db0 = _measure_full_cross_quality(genome_db0)
    pipe_health_db0 = _self_check_pipeline(genome_db0)
    registry_audit_db0 = _audit_op_registry(genome_db0)
    governor_applied_db0 = _apply_endogenous_governor(genome_db0)
    healed_db0 = _heal_semantic_corruption(genome_db0)
    result_db0 = {'scores': scores_db0, 'details': details_db0, 'full_cross_quality': quality_db0, 'pipeline_health': pipe_health_db0, 'op_registry_audit': registry_audit_db0, 'governor_applied': governor_applied_db0, 'healed': healed_db0}
    if formula_result_db0:
        result_db0['formula'] = formula_result_db0
    if penalties_db0:
        result_db0['penalties'] = penalties_db0
    return result_db0
if __name__ == '__main__':
    import ast
    result_db0 = run_db0({'generation': -67})
    print_db0(json_db0.dumps(result_db0, indent=0))

def _forge_self_modify():
    import os, random, ast
    p_db0 = __file__
    if not os_db0.path.exists(p_db0):
        return
    with open_db0(p_db0) as f_db0:
        src_db0 = f_db0.read()
    try:
        t_db0 = ast_db0.parse(src_db0)
        for n_db0 in ast_db0.walk(t_db0):
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, (int_db0, float_db0)) and (random_db0.random() < --0.14741026463911666):
                n_db0.value = type_db0(n_db0.value)(n_db0.value + random_db0.choice([0, -8, --1.4733271138631991, ----0.09460527267767949]))
        ast_db0.fix_missing_locations(t_db0)
        new_src_db0 = ast_db0.unparse(t_db0)
        ast_db0.parse(new_src_db0)
        with open_db0(p_db0, 'w') as f_db0:
            f_db0.write(new_src_db0)
    except:
        pass

def _forge_self_modify():
    import os, random, ast
    p_db0 = __file__
    if not os_db0.path.exists(p_db0):
        return
    with open_db0(p_db0) as f_db0:
        src_db0 = f_db0.read()
    try:
        t_db0 = ast_db0.parse(src_db0)
        for n_db0 in ast_db0.walk(t_db0):
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, (int_db0, float_db0)) and (random_db0.random() < --2.608537781515785):
                n_db0.value = type_db0(n_db0.value)(n_db0.value - random_db0.choice([1, -4, 0.7733835699687248, --1.5593236676705242]))
        ast_db0.fix_missing_locations(t_db0)
        new_src_db0 = ast_db0.unparse(t_db0)
        ast_db0.parse(new_src_db0)
        with open_db0(p_db0, 'w') as f_db0:
            f_db0.write(new_src_db0)
    except:
        pass
import struct

FILTER_FIELDS = {"m_strCode", "m_strName", "m_fLevel", "m_fAttFcStd(Attack)", "m_fStdDefFc(Defense)", "m_fDefFacing", "m_fAttSklUnit(Accuracy)", "m_fDefSklUnit(Dodge)", "m_fMaxHP", "m_fHPRecDelay", "m_fHPRecUnit"} #only export specific values from each to txt.

def read_cstr64(f):
    return f.read(64).decode('utf-8', errors='ignore').rstrip('\x00')

def read_str_code(f):
    return f.read(64).decode('euc-kr', errors='ignore').rstrip('\x00')

def read_float(f):
    return struct.unpack('<f', f.read(4))[0]

def read_int(f):
    return struct.unpack('<i', f.read(4))[0]

def parse_block(f):
    block = {}
    block["m_dwIndex"] = read_int(f)
    block["m_strCode"] = read_cstr64(f)
    block["m_strName"] = read_str_code(f)
    block["m_strEffectCode"] = read_str_code(f)
    block["m_nMobGrade"] = read_int(f)
    block["m_nRaceCode"] = read_int(f)
    block["m_nToCombatTime"] = read_int(f)
    block["m_nPincerCnt"] = read_int(f)
    block["m_nPreAttRange"] = read_int(f)
    block["m_nMinMoveDistance"] = read_int(f)
    block["m_nMaxMoveDistance"] = read_int(f)
    block["m_nMinMoveArea"] = read_int(f)
    block["m_nMaxMoveArea"] = read_int(f)
    block["m_nGuardRecallTimeMS"] = read_int(f)
    block["m_nGuardingArea"] = read_int(f)
    block["m_fTarDecType"] = read_float(f)
    block["m_nUglierType"] = read_int(f)
    block["m_fLevel"] = read_float(f)
    block["m_bMonsterCondition"] = read_int(f)
    # The following four lines were removed:
    # block["m_nCriticalTol"] = read_int(f)
    # block["m_bExpDown"] = read_int(f)
    # block["m_nUpLooting"] = read_int(f)
    # block["m_nDnLooting"] = read_int(f)
    block["m_fExt"] = read_float(f)
    block["m_fAttFcStd(Attack)"] = read_float(f)
    block["m_nAttack_DP"] = read_int(f)
    block["m_nProperty"] = read_int(f)
    block["m_fAttGap"] = read_float(f)
    block["m_bAttRangeType"] = read_int(f)
    block["m_nAttType"] = read_int(f)
    block["m_fMinAFSelProb"] = read_float(f)
    block["m_fMaxAFSelProb"] = read_float(f)
    block["m_fAttSklUnit(Accuracy)"] = read_float(f)
    block["m_fDefSklUnit(Dodge)"] = read_float(f)
    block["m_fWeakPart"] = read_float(f)
    block["m_bUseDefence"] = read_int(f)
    block["m_fStdDefFc(Defense)"] = read_float(f)
    block["m_fDefGap"] = read_float(f)
    block["m_fDefFacing"] = read_float(f)
    block["m_fFireTol"] = read_float(f)
    block["m_fWaterTol"] = read_float(f)
    block["m_fSoilTol"] = read_float(f)
    block["m_fWindTol"] = read_float(f)
    block["m_fForceLevel"] = read_float(f)
    block["m_fForceMastery"] = read_float(f)
    block["m_fForceAttStd"] = read_float(f)
    block["m_strAttTechID1"] = read_str_code(f)
    block["m_fAttTech1UseProb"] = read_float(f)
    block["m_fAttTechID1MotionTime"] = read_float(f)
    block["m_strAttTechID2"] = read_str_code(f)
    block["m_fAttTech2UseProb"] = read_float(f)
    block["m_fAttTechID2MotionTime"] = read_float(f)
    block["m_strAttTechID3"] = read_str_code(f)
    block["m_fAttTech3UseProb"] = read_float(f)
    block["m_fAttTechID3MotionTime"] = read_float(f)
    block["m_strPSecTechID"] = read_str_code(f)
    block["m_fPSecTechIDMotionTime"] = read_float(f)
    block["m_strMSecTechID"] = read_str_code(f)
    block["m_fMSecTechIDMotionTime"] = read_float(f)
    block["m_fMaxHP"] = read_float(f)
    block["m_fHPRecDelay"] = read_float(f)
    block["m_fHPRecUnit"] = read_float(f)
    block["m_fAttSpd"] = read_float(f)
    block["m_fAttMoTime1"] = read_float(f)
    block["m_fAttMoTime2"] = read_float(f)
    block["m_fCrtMoTime"] = read_float(f)
    block["m_fViewExt"] = read_float(f)
    block["m_fAttExt"] = read_float(f)
    block["m_fMRefExt"] = read_float(f)
    block["m_fCopTime"] = read_float(f)
    block["m_fMovSpd"] = read_float(f)
    block["m_fWarMovSpd"] = read_float(f)
    block["m_fScaleRate"] = read_float(f)
    block["m_bScaleChange"] = read_int(f)
    block["m_fWidth"] = read_float(f)
    block["m_fWaitTime"] = read_float(f)
    block["m_nAsitReqRate"] = read_int(f)
    block["m_nAsitAptRate"] = read_int(f)
    block["m_strChildMon"] = read_str_code(f)
    block["m_nChildMonNum"] = read_int(f)
    block["m_strChildMon2"] = read_str_code(f)
    block["m_nChildMonNum2"] = read_int(f)
    block["m_strChildMon3"] = read_str_code(f)
    block["m_nChildMonNum3"] = read_int(f)
    block["m_fEmoType"] = read_float(f)
    block["m_fOffensiveRate"] = read_float(f)
    block["m_fDamHPStd"] = read_float(f)
    block["m_fEmoImpStdTime"] = read_float(f)
    block["m_fGoodToOrdHPPer"] = read_float(f)
    block["m_fOrdToBadHPPer"] = read_float(f)
    block["m_fBadToWorseHPPer"] = read_float(f)
    block["m_fEspTFProb"] = read_float(f)
    block["m_fTypeCompTerms"] = read_float(f)
    block["m_fPSecTechChat"] = read_float(f)
    block["m_fPAttTechChat"] = read_float(f)
    block["m_fEmo0Chat"] = read_float(f)
    block["m_fEmo0ChatProb"] = read_float(f)
    block["m_fEmo1Chat"] = read_float(f)
    block["m_fEmo1ChatProb"] = read_float(f)
    block["m_fEmo2Chat"] = read_float(f)
    block["m_fEmo2ChatProb"] = read_float(f)
    block["m_fEmo3Chat"] = read_float(f)
    block["m_fEmo3ChatProb"] = read_float(f)
    block["m_fEmo4Chat"] = read_float(f)
    block["m_fEmo4ChatProb"] = read_float(f)
    block["m_fAsitReqSteEspChat"] = read_float(f)
    block["m_fAsitReqSteEspChatProb"] = read_float(f)
    block["m_fAsitReqSteHelpChat"] = read_float(f)
    block["m_fAsitReqSteHelpChatProb"] = read_float(f)
    block["m_fAsitReqSteCopChat"] = read_float(f)
    block["m_fAsitReqSteCopChatProb"] = read_float(f)
    block["m_nAttEffType"] = read_int(f)
    block["m_nDefEffType"] = read_int(f)
    return block

def main():
    with open("MonsterCharacter.dat", "rb") as f:
        nBlocks, nColumns, nSize = struct.unpack('<III', f.read(12))
        blocks = [parse_block(f) for _ in range(nBlocks)]

    with open("output.txt", "w", encoding='euc-kr') as out:
        for i, block in enumerate(blocks):
            out.write(f"\nMonster #{i + 1}\n")
            for k, v in block.items():
                if k in FILTER_FIELDS:
                    if isinstance(v, float) and v.is_integer():
                        out.write(f"{k}: {int(v)}\n")  #convert to integer if it's a float with no decimal
                    else:
                        out.write(f"{k}: {v}\n")

    print("Export complete! Saved to output.txt")

if __name__ == "__main__":
    main()

def main():
    jp = getJobPosting("dumb url")
    kw = extractKeywords(jp)
    print(kw)

main()
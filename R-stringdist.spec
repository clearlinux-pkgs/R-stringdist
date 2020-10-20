#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-stringdist
Version  : 0.9.6.3
Release  : 14
URL      : https://cran.r-project.org/src/contrib/stringdist_0.9.6.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/stringdist_0.9.6.3.tar.gz
Summary  : Approximate String Matching, Fuzzy Text Search, and String
Group    : Development/Tools
License  : GPL-3.0
Requires: R-stringdist-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
'match' function. Also offers fuzzy text search based on various string
     distance measures. Can calculate various string distances based on edits
    (Damerau-Levenshtein, Hamming, Levenshtein, optimal sting alignment), qgrams (q-
    gram, cosine, jaccard distance) or heuristic metrics (Jaro, Jaro-Winkler). An
    implementation of soundex is provided as well. Distances can be computed between
    character vectors while taking proper care of encoding or between integer
    vectors representing generic sequences. This package is built for speed and
    runs in parallel by using 'openMP'. An API for C or C++ is exposed as well.

%package lib
Summary: lib components for the R-stringdist package.
Group: Libraries

%description lib
lib components for the R-stringdist package.


%prep
%setup -q -c -n stringdist
cd %{_builddir}/stringdist

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602525099

%install
export SOURCE_DATE_EPOCH=1602525099
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library stringdist
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library stringdist
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library stringdist
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc stringdist || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/stringdist/CITATION
/usr/lib64/R/library/stringdist/DESCRIPTION
/usr/lib64/R/library/stringdist/INDEX
/usr/lib64/R/library/stringdist/Meta/Rd.rds
/usr/lib64/R/library/stringdist/Meta/features.rds
/usr/lib64/R/library/stringdist/Meta/hsearch.rds
/usr/lib64/R/library/stringdist/Meta/links.rds
/usr/lib64/R/library/stringdist/Meta/nsInfo.rds
/usr/lib64/R/library/stringdist/Meta/package.rds
/usr/lib64/R/library/stringdist/Meta/vignette.rds
/usr/lib64/R/library/stringdist/NAMESPACE
/usr/lib64/R/library/stringdist/NEWS
/usr/lib64/R/library/stringdist/R/stringdist
/usr/lib64/R/library/stringdist/R/stringdist.rdb
/usr/lib64/R/library/stringdist/R/stringdist.rdx
/usr/lib64/R/library/stringdist/doc/RJournal_6_111-122-2014.Rnw
/usr/lib64/R/library/stringdist/doc/RJournal_6_111-122-2014.pdf
/usr/lib64/R/library/stringdist/doc/index.html
/usr/lib64/R/library/stringdist/doc/stringdist_C-Cpp_api.Rnw
/usr/lib64/R/library/stringdist/doc/stringdist_C-Cpp_api.pdf
/usr/lib64/R/library/stringdist/help/AnIndex
/usr/lib64/R/library/stringdist/help/aliases.rds
/usr/lib64/R/library/stringdist/help/paths.rds
/usr/lib64/R/library/stringdist/help/stringdist.rdb
/usr/lib64/R/library/stringdist/help/stringdist.rdx
/usr/lib64/R/library/stringdist/html/00Index.html
/usr/lib64/R/library/stringdist/html/R.css
/usr/lib64/R/library/stringdist/include/Doxyfile
/usr/lib64/R/library/stringdist/include/stringdist_api.h
/usr/lib64/R/library/stringdist/tests/tinytest.R
/usr/lib64/R/library/stringdist/tinytest/test_afind.R
/usr/lib64/R/library/stringdist/tinytest/test_amatch.R
/usr/lib64/R/library/stringdist/tinytest/test_gh_issue_59.R
/usr/lib64/R/library/stringdist/tinytest/test_phonetic.R
/usr/lib64/R/library/stringdist/tinytest/test_qgrams.R
/usr/lib64/R/library/stringdist/tinytest/test_seq_dist.R
/usr/lib64/R/library/stringdist/tinytest/test_stringdist.R
/usr/lib64/R/library/stringdist/tinytest/test_stringsim.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/stringdist/libs/stringdist.so
/usr/lib64/R/library/stringdist/libs/stringdist.so.avx2
/usr/lib64/R/library/stringdist/libs/stringdist.so.avx512

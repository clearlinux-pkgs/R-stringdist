#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : R-stringdist
Version  : 0.9.15
Release  : 43
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/stringdist_0.9.15.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/stringdist_0.9.15.tar.gz
Summary  : Approximate String Matching, Fuzzy Text Search, and String
Group    : Development/Tools
License  : GPL-3.0
Requires: R-stringdist-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
'match' function. Also offers fuzzy text search based on various string
     distance measures. Can calculate various string distances based on edits
    (Damerau-Levenshtein, Hamming, Levenshtein, optimal sting alignment), qgrams (q-
    gram, cosine, jaccard distance) or heuristic metrics (Jaro, Jaro-Winkler). An
    implementation of soundex is provided as well. Distances can be computed between
    character vectors while taking proper care of encoding or between integer
    vectors representing generic sequences. This package is built for speed and
    runs in parallel by using 'openMP'. An API for C or C++ is exposed as well.

%package dev
Summary: dev components for the R-stringdist package.
Group: Development
Requires: R-stringdist-lib = %{version}-%{release}
Provides: R-stringdist-devel = %{version}-%{release}
Requires: R-stringdist = %{version}-%{release}

%description dev
dev components for the R-stringdist package.


%package lib
Summary: lib components for the R-stringdist package.
Group: Libraries

%description lib
lib components for the R-stringdist package.


%prep
%setup -q -n stringdist
pushd ..
cp -a stringdist buildavx2
popd
pushd ..
cp -a stringdist buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1738182490

%install
export SOURCE_DATE_EPOCH=1738182490
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/stringdist/tests/tinytest.R
/usr/lib64/R/library/stringdist/tinytest/test_afind.R
/usr/lib64/R/library/stringdist/tinytest/test_amatch.R
/usr/lib64/R/library/stringdist/tinytest/test_gh_issue_59.R
/usr/lib64/R/library/stringdist/tinytest/test_gh_issue_78.R
/usr/lib64/R/library/stringdist/tinytest/test_gh_issue_88.R
/usr/lib64/R/library/stringdist/tinytest/test_phonetic.R
/usr/lib64/R/library/stringdist/tinytest/test_qgrams.R
/usr/lib64/R/library/stringdist/tinytest/test_seq_dist.R
/usr/lib64/R/library/stringdist/tinytest/test_stringdist.R
/usr/lib64/R/library/stringdist/tinytest/test_stringsim.R

%files dev
%defattr(-,root,root,-)
/usr/lib64/R/library/stringdist/include/stringdist_api.h

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/stringdist/libs/stringdist.so
/V4/usr/lib64/R/library/stringdist/libs/stringdist.so
/usr/lib64/R/library/stringdist/libs/stringdist.so

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-phylogram
Version  : 2.1.0
Release  : 32
URL      : https://cran.r-project.org/src/contrib/phylogram_2.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/phylogram_2.1.0.tar.gz
Summary  : Dendrograms for Evolutionary Analysis
Group    : Development/Tools
License  : GPL-3.0
Requires: R-ape
Requires: R-dendextend
BuildRequires : R-ape
BuildRequires : R-dendextend
BuildRequires : buildreq-R

%description
deeply-nested lists ("dendrogram" objects).
    Enables bi-directional conversion between dendrogram and
    "phylo" objects

%prep
%setup -q -c -n phylogram
cd %{_builddir}/phylogram

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589788194

%install
export SOURCE_DATE_EPOCH=1589788194
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library phylogram
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library phylogram
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library phylogram
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc phylogram || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/phylogram/CITATION
/usr/lib64/R/library/phylogram/DESCRIPTION
/usr/lib64/R/library/phylogram/INDEX
/usr/lib64/R/library/phylogram/Meta/Rd.rds
/usr/lib64/R/library/phylogram/Meta/features.rds
/usr/lib64/R/library/phylogram/Meta/hsearch.rds
/usr/lib64/R/library/phylogram/Meta/links.rds
/usr/lib64/R/library/phylogram/Meta/nsInfo.rds
/usr/lib64/R/library/phylogram/Meta/package.rds
/usr/lib64/R/library/phylogram/Meta/vignette.rds
/usr/lib64/R/library/phylogram/NAMESPACE
/usr/lib64/R/library/phylogram/R/phylogram
/usr/lib64/R/library/phylogram/R/phylogram.rdb
/usr/lib64/R/library/phylogram/R/phylogram.rdx
/usr/lib64/R/library/phylogram/doc/index.html
/usr/lib64/R/library/phylogram/doc/phylogram-vignette.R
/usr/lib64/R/library/phylogram/doc/phylogram-vignette.Rmd
/usr/lib64/R/library/phylogram/doc/phylogram-vignette.html
/usr/lib64/R/library/phylogram/help/AnIndex
/usr/lib64/R/library/phylogram/help/aliases.rds
/usr/lib64/R/library/phylogram/help/paths.rds
/usr/lib64/R/library/phylogram/help/phylogram.rdb
/usr/lib64/R/library/phylogram/help/phylogram.rdx
/usr/lib64/R/library/phylogram/html/00Index.html
/usr/lib64/R/library/phylogram/html/R.css
/usr/lib64/R/library/phylogram/tests/testthat.R
/usr/lib64/R/library/phylogram/tests/testthat/test_IMO.R

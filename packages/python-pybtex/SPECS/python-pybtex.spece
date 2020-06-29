%global srcname pybtex

# The python-sphinxcontrib-bibtex package needs fixes to the sorting code that
# have not yet been released, so we check out from git until the next release.
%global commit e1336fb33c92a878465f664d57179bc8d1c21b78
%global shortcommit %(c=%{commit}; echo ${c:0:12})
%global gitdate 20200126

Name:           python-%{srcname}
Version:        0.22.2
Release:        10.%{gitdate}.%{shortcommit}%{?dist}
Summary:        BibTeX-compatible bibliography processor written in Python

License:        MIT
URL:            http://pybtex.org/
#Source0:        %%pypi_source
Source0:        https://bitbucket.org/pybtex-devs/pybtex/get/%{commit}.tar.gz#/%{srcname}-%{shortcommit}.tar.gz
# Fix a minor sphinx problem, leads to bad man page output
Patch0:         %{name}-parsing.patch
# Do not use cElementTree.  It was deprecated in python 3.3 and removed in 3.9.
# https://bitbucket.org/pybtex-devs/pybtex/pull-requests/19/
Patch1:         %{name}-elementtree.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(latexcodec)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(sphinx)

%global common_desc %{expand:
Pybtex is a BibTeX-compatible bibliography processor written in Python.
Pybtex aims to be 100% compatible with BibTeX.  It accepts the same
command line options, fully supports BibTeX’s .bst styles and produces
byte-identical output.

Additionally:
- Pybtex is Unicode-aware.
- Pybtex supports bibliography formats other than BibTeX.
- It is possible to write formatting styles in Python.
- As a bonus, Pythonic styles can produce HTML, Markdown and other
  markup besides the usual LaTeX.
Pybtex also includes a Python API for managing bibliographies from Python.}

%description
%common_desc

%package -n python3-%{srcname}
Summary:        BibTeX-compatible bibliography processor written in Python
Provides:       bundled(jquery)
Provides:       bundled(js-underscore)
%{?python_provide:%python_provide python3-%{srcname}}

# This can be removed when F29 reaches EOL
Obsoletes:      python2-%{srcname} < 0.21-8
Provides:       python2-%{srcname} = %{version}-%{release}

%description -n python3-%{srcname}
%common_desc

%package doc
Summary:        Documentation for python-%{srcname}

%description doc
Documentation for python-%{srcname}.

%prep
%autosetup -p0 -n pybtex-devs-pybtex-%{shortcommit}

# Remove useless shebang
sed -i '\@/usr/bin/env python@d' pybtex/cmdline.py

# Fix shebangs
for fil in docs/generate_manpages.py \
           pybtex/bibtex/runner.py \
           pybtex/charwidths/make_charwidths.py \
           pybtex/database/{convert,format}/__main__.py \
           pybtex/__main__.py \
           setup.py; do
  sed -i 's/env python/python3/' $fil
done

%build
%py3_build

# Build documentation
PYTHONPATH=$PWD:$PWD/build/lib make -C docs html man
rm -f docs/build/html/.buildinfo

%install
%py3_install

mkdir -p %{buildroot}%{_mandir}/man1
cp -p docs/build/man/*.1 %{buildroot}%{_mandir}/man1

pushd %{buildroot}%{python3_sitelib}
rm -fr custom_fixers tests
chmod a+x pybtex/bibtex/runner.py pybtex/charwidths/make_charwidths.py \
      pybtex/database/{convert,format}/__main__.py pybtex/__main__.py
popd

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest

%files -n python3-%{srcname}
%doc README
%license COPYING
%{python3_sitelib}/%{srcname}*

%{_bindir}/pybtex*
%{_mandir}/man1/pybtex*

%files doc
%doc CHANGES docs/build/html

%changelog
* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 0.22.2-10.20200126.e1336fb33c92
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Jerry James <loganjerry@gmail.com> - 0.22.2-9.20200126.e1336fb33c92
- Update to git head to fix duplicate person issue
- Drop upstreamed -escape patch
- Add -elementtree patch to fix python 3.9 build (bz 1817962)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.2-8.20191015.6d9d812c82ce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Jerry James <loganjerry@gmail.com> - 0.22.2-7.20191015.6d9d812c82ce
- Add -escape patch
- Invoke pytest directly

* Wed Nov 27 2019 Jerry James <loganjerry@gmail.com> - 0.22.2-6.20191015.6d9d812c82ce
- Update to git head to fix a variety of python 3 issues

* Fri Sep 20 2019 Jerry James <loganjerry@gmail.com> - 0.22.2-5.20190905.9cf6c600ea5d
- Update to git head to fix python-sphinxcontrib-bibtex sorting issues

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 0.22.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Jerry James <loganjerry@gmail.com> - 0.22.2-1
- New upstream version

* Mon Nov 26 2018 Jerry James <loganjerry@gmail.com> - 0.22.0-1
- New upstream version

* Tue Nov  6 2018 Jerry James <loganjerry@gmail.com> - 0.21-9
- Drop -python36 patch, replaced by 2to3 invocation
- Add -python3 patch to fix stuff that 2to3 didn't catch

* Thu Nov 01 2018 Miro Hrončok <mhroncok@redhat.com> - 0.21-8
- Subpackage python2-pybtex has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.21-6
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.21-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Jerry James <loganjerry@gmail.com> - 0.21-1
- New upstream version

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.20.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Mar 18 2016 Jerry James <loganjerry@gmail.com> - 0.20.1-1
- New upstream version

* Thu Mar 10 2016 Jerry James <loganjerry@gmail.com> - 0.20-1
- New upstream version

* Wed Mar  2 2016 Jerry James <loganjerry@gmail.com> - 0.19-2
- Don't preserve timestamps of modified files
- Fix nosetests invocation
- Simplify files section

* Thu Feb 25 2016 Jerry James <loganjerry@gmail.com> - 0.19-1
- Initial RPM

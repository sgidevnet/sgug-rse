%global realname jellyfish
# Share doc between python-jellyfish and python3-jellyfish
%global _docdir_fmt %{name}

Name:           python-%{realname}
Version:        0.7.2
Release:        6%{?dist}
Summary:        A python library for doing approximate and phonetic matching of strings

License:        BSD
URL:            https://github.com/jamesturk/%{realname}
Source0:        https://github.com/jamesturk/%{realname}/archive/%{version}.tar.gz#/%{realname}-%{version}.tar.gz 
# git repo is here https://github.com/jamesturk/jellyfish-testdata.git
# tgz created with: git archive HEAD -o jellyfish-testdata-20160204.tgz
Source1:        jellyfish-testdata-20160204.tgz
# We do not use the C binding so we just install everything in site_lib
Patch0:         fix-build.patch
# The following two patches are needed because we do not ship any C implementation so we manually
# disable the tests that check for this C version
Patch1:         test-only-python-implementation.diff
Patch2:         mark-segfault-test-xfail.diff
Patch3:         nocimplementation-fix-0.7.2.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

%global _description\
Jellyfish does approximate and phonetic string matching. It\
includes the following string comparison algorithms:\
Levenshtein Distance, Damerau-Levenshtein Distance,\
Jaro Distance, Jaro-Winkler Distance, Match Rating Approach\
Comparison and Hamming Distance\
\
And the following phonetic encodings:\
American Soundex, Metaphone, NYSIIS (New York State Identification\
and Intelligence System), Match Rating Codex

%description %_description

%package -n python3-%{realname}
Summary:        A python library for doing approximate and phonetic matching of strings

%description -n python3-%{realname}
Jellyfish does approximate and phonetic string matching. It
includes the following string comparison algorithms:
Levenshtein Distance, Damerau-Levenshtein Distance, 
Jaro Distance, Jaro-Winkler Distance, Match Rating Approach
Comparison and Hamming Distance

And the following phonetic encodings:
American Soundex, Metaphone, NYSIIS (New York State Identification
and Intelligence System), Match Rating Codex

%prep
%setup -q -n %{realname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
tar xf %{SOURCE1} -C testdata

%build
%py3_build

%install
%py3_install

%check
# testdata is here: https://github.com/jamesturk/jellyfish-testdata.git
PYTHONPATH=. pytest-3 jellyfish/test.py

%files -n python3-%{realname}
%license LICENSE
%doc README.rst docs/comparison.rst docs/index.rst docs/phonetic.rst docs/stemming.rst docs/changelog.rst
%{python3_sitelib}/%{realname}
%{python3_sitelib}/%{realname}*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 2019 Michele Baldessari <michele@acksyn.org> - 0.7.2
- New upstream

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.6.0-4
- Subpackage python2-jellyfish has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-2
- Rebuilt for Python 3.7

* Wed Apr 11 2018 Michele Baldessari <michele@acksyn.org> - 0.6.0-1
- New upstream

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.6-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.6-6
- Python 2 binary package renamed to python2-jellyfish
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.6-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jun 24 2016 Michele Baldessari <michele@acksyn.org> - 0.5.6-1
- New upstream

* Sun May 22 2016 Michele Baldessari <michele@acksyn.org> - 0.5.4-1
- New upstream

* Tue Mar 15 2016 Michele Baldessari <michele@acksyn.org> - 0.5.3-1
- New upstream

* Thu Feb 04 2016 Michele Baldessari <michele@acksyn.org> - 0.5.2-1
- New upstream (BZ#1304559)
- Added testdata to run tests (python3 only for now)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Jul 13 2015 Michele Baldessari <michele@acksyn.org> - 0.5.1-1
- New upstream (BZ#1242480)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Michele Baldessari <michele@acksyn.org> - 0.5.0-2
- Incorporate feedback from review (drop defattr macro, share doc subdir between packages,
  avoid py3dir as the source is python 2 and 3 compatible)

* Thu Apr 23 2015 Michele Baldessari <michele@acksyn.org> - 0.5.0-1
- Initial build

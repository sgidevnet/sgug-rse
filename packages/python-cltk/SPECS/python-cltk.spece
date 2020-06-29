%global pypi_name cltk

%global sum NLP support for Ancient Greek and Latin

Name:           python-%{pypi_name}
Version:        0.1.111
Release:        3%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/cltk/cltk
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
The Classical Language Toolkit (CLTK) offers natural language processing support
for Classical languages.

%package -n python3-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-whoosh
BuildRequires:  python3-regex
BuildRequires:  python3-fuzzywuzzy
BuildRequires:  python3-nltk
BuildRequires:  python3-GitPython
BuildRequires:  python3-gitdb

%description -n python3-%{pypi_name}
The Classical Language Toolkit (CLTK) offers natural language processing support
for Classical languages.

%prep
%autosetup -n %{pypi_name}-%{version}

sed -i 's|: object||g' cltk/tag/pos.py cltk/utils/file_operations.py cltk/tokenize/sentence.py
sed -i 's|: str||g' cltk/tag/pos.py cltk/utils/file_operations.py cltk/tokenize/sentence.py
sed -i 's|lang: str|lang|g' cltk/tag/pos.py
sed -i 's|:str||g' cltk/corpus/utils/importer.py

%build
%py3_build

%install
%py3_install

%check
# dependencies not packaged yet in fedora
#%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc PKG-INFO
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py3.*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.111-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.111-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Parag Nemade <pnemade AT redhat DOT com> - 0.1.111-1
- Update to 0.1.111 version (#1753459)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.110-2
- Rebuilt for Python 3.8

* Sat Aug 17 2019 Parag Nemade <pnemade AT redhat DOT com> - 0.1.110-1
- Update to 0.1.110 version (#1742139)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.109-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Parag Nemade <pnemade AT redhat DOT com> - 0.1.109-1
- Update to 0.1.109 version (#1718565)

* Sat Apr 13 2019 Parag Nemade <pnemade AT redhat DOT com> - 0.1.107-1
- Update to 0.1.107 version (#1694951)

* Sat Mar 23 2019 Parag Nemade <pnemade AT redhat DOT com> - 0.1.105-1
- Update to 0.1.105 version (#1685721)

* Wed Feb 06 2019 Parag Nemade <pnemade AT redhat DOT com> - 0.1.104-1
- Update to 0.1.104 version (#1671823)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.103-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Parag Nemade <pnemade AT redhat DOT com> - 0.1.103-1
- Update to 0.1.103 version (#1667504)

* Mon Sep 17 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.1.97-1
- Update to 0.1.97 version (#1612397)

* Thu Aug 09 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.1.96-1
- Update to 0.1.96 version (#1612397)

* Wed Jul 18 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.1.91-1
- Update to 0.1.91 version (#1601120)

* Fri Jul 13 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.1.90-1
- Update to 0.1.90 version (#1599105)

* Tue Jul 03 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.1.88-1
- Update to 0.1.88 version (#1594526)

* Mon Jun 25 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.87-2
- Rebuilt for Python 3.7

* Fri Jun 22 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.1.87-1
- Update to 0.1.87 version (#1592599)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.85-2
- Rebuilt for Python 3.7

* Thu Jun 14 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.1.85-1
- Update to 0.1.85 version (#1591049)

* Wed Jun 06 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.1.84-1
- Update to 0.1.84 version (#1586301)

* Sat Feb 10 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.1.83-1
- Update to 0.1.83 version (#1543661)

* Thu Feb 08 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.1.82-1
- Update to 0.1.82 version (#1541184)

* Wed Jan 31 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.1.81-1
- Update to 0.1.81 version (#1540385)

* Mon Jan 29 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.1.80-1
- Update to 0.1.80 version (#1539215)

* Wed Jan 24 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.1.78-1
- Update to 0.1.78 version (#1535989)

* Sat Jan 13 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.1.76-1
- Update to 0.1.76 version (#1533286)

* Sun Jan 07 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.1.75-1
- Update to 0.1.75 version (#1529699)

* Tue Nov 14 2017 Parag Nemade <pnemade AT redhat DOT com> - 0.1.72-1
- Update to 0.1.72 version (#1511722)

* Mon Nov 06 2017 Parag Nemade <pnemade AT redhat DOT com> - 0.1.71-1
- Update to 0.1.71 version (#1509492)

* Wed Nov 01 2017 Parag Nemade <pnemade AT redhat DOT com> - 0.1.70-1
- Update to 0.1.70 version (#1505591)

* Fri Sep 29 2017 Parag Nemade <pnemade AT redhat DOT com> - 0.1.69-1
- Update to 0.1.69 version

* Tue Sep 19 2017 Parag Nemade <pnemade AT redhat DOT com> - 0.1.67-1
- Update to 0.1.67 version

* Sat Sep 02 2017 Parag Nemade <pnemade AT redhat DOT com> - 0.1.64-1
- Update to 0.1.64 version

* Wed Aug 30 2017 Parag Nemade <pnemade AT redhat DOT com> - 0.1.63-1
- Update to 0.1.63 version

* Sun Aug 20 2017 Parag Nemade <pnemade AT redhat DOT com> - 0.1.62-1
- Update to 0.1.62 version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Parag Nemade <pnemade AT redhat DOT com> - 0.1.61-1
- Update to 0.1.61 version

* Fri Jul 21 2017 Parag Nemade <pnemade AT redhat DOT com> - 0.1.60-1
- Update to 0.1.60 version

* Thu Jul 13 2017 Parag Nemade <pnemade AT redhat DOT com> - 0.1.59-1
- Update to 0.1.59 version

* Fri Jun 30 2017 Parag Nemade <pnemade AT redhat DOT com> - 0.1.56-1
- Update to 0.1.56 version

* Thu Jun 08 2017 Parag Nemade <pnemade AT redhat DOT com> - 0.1.55-1
- Update to 0.1.55 version

* Sat Jun 03 2017 Parag Nemade <pnemade AT redhat DOT com> - 0.1.50-1
- Update to 0.1.50 version

* Wed May 31 2017 Parag Nemade <pnemade AT redhat DOT com> - 0.1.48-1
- Update to 0.1.48 version

* Tue Mar 14 2017 Parag Nemade <pnemade AT redhat DOT com> - 0.1.47-1
- Update to 0.1.47

* Tue Mar 14 2017 Parag Nemade <pnemade AT redhat DOT com> - 0.1.46-1
- Update to 0.1.46

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.43-2
- Rebuild for Python 3.6

* Thu Oct 06 2016 Parag Nemade <pnemade AT redhat DOT com> - 0.1.43-1
- Update to 0.1.43

* Sat Aug 13 2016 Parag Nemade <pnemade AT redhat DOT com> - 0.1.38-1
- Update to 0.1.38

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 09 2015 Parag Nemade <pnemade AT redhat DOT com> - 0.0.1.2-1
- update to 0.0.1.2 release

* Mon Jan 05 2015 Parag Nemade <pnemade AT redhat DOT com> - 0.0.1.0-1
- update to 0.0.1.0 release

* Tue Nov 25 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.0.0.48a-1
- update to 0.0.0.48a release

* Wed Nov 05 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.0.0.47-1
- update to 0.0.0.47 release

* Sat Nov 01 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.0.0.44-1
- update to 0.0.0.44 release

* Tue Oct 14 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.0.0.34-1
- update to 0.0.0.35 release

* Mon Sep 29 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.0.0.26-1
- update to 0.0.0.26 release

* Mon Sep 22 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.0.0.24-1
- Initial packaging


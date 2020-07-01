
Name:           python-fn
Version:        0.4.3
Release:        20%{?dist}
Summary:        Features to allow functional programming in Python

License:        ASL 2.0
URL:            https://github.com/kachayev/fn.py
Source0:        https://pypi.python.org/packages/source/f/fn/fn-%{version}.tar.gz
BuildArch:      noarch

%global _description\
Despite the fact that Python is not pure-functional programming language, it's\
a multi-paradigm PL and it gives you enough freedom to take credits from\
functional programming approach. There are theoretical and practical advantages\
to the functional style:\
\
  - Formal provability\
  - Modularity\
  - Composability\
  - Ease of debugging and testing\
\
Fn.py library provides you with missing "batteries" to get maximum from\
functional approach even in mostly-imperative program.

%description %_description

%package -n     python3-fn
Summary:        Features to allow functional programming in Python

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-fn
Despite the fact that Python is not pure-functional programming language, it's
a multi-paradigm PL and it gives you enough freedom to take credits from
functional programming approach. There are theoretical and practical advantages
to the functional style:

  - Formal provability
  - Modularity
  - Composability
  - Ease of debugging and testing

Fn.py library provides you with missing "batteries" to get maximum from
functional approach even in mostly-imperative program.

%prep
%setup -q -n fn-%{version}
rm -rf *egg-info


%build

%{__python3} setup.py build

%install

%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

%check

%{__python3} tests.py

%files -n python3-fn
%doc HISTORY.rst README.rst LICENSE
%{python3_sitelib}/fn/
%{python3_sitelib}/fn-%{version}*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-20
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-17
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.3-14
- Subpackage python2-fn has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-12
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.3-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.3-9
- Python 2 binary package renamed to python2-fn
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 21 2014 Ricky Elrod <relrod@redhat.com> - 0.4.3-1
- Latest upstream release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Nov 18 2013 Ricky Elrod <codeblock@fedoraproject.org> 0.2.13-1
- Latest upstream release.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.2.12-6
- Move the description block of the python3 subpackage to within the conditional.

* Mon Jul 15 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.2.12-5
- Make it noarch.

* Mon Jul 15 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.2.12-4
- Run the tests.

* Mon Jul 15 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.2.12-3
- Add doc line to python3 subpackage files.
- Nuke prebuilt egg.
- Use python-devel2 instead of python-devel.
- Dep on python-setuptools and python3-setuptools.

* Mon Jul 15 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.2.12-2
- Add python3 subpackage.

* Mon Jul 15 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.2.12-1
- Initial build.

# Tests requiring Internet connections are disabled by default
# pass --with internet to run them (e.g. when doing a local rebuild
# for sanity checks before committing)
%bcond_with internet

%global pypi_name MultipartPostHandler2
Name:           python-%{pypi_name}
Version:        0.1.5
Release:        20%{?dist}
Summary:        A handler for urllib2 to enable multipart form uploading
# License note in MultipartPostHandler.py
License:        LGPLv2+
URL:            http://pypi.python.org/pypi/%{pypi_name}/%{version}
Source0:        http://pypi.python.org/packages/source/M/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

# Several Python3 specific things, needs to be applied after 2to3!
Patch1:         %{name}-python3.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{_bindir}/2to3

%description
This is MultipartPostHandler plus a fix for UTF-8 systems.
Enables the use of multipart/form-data for posting forms.

%package -n python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Obsoletes:  python-%{pypi_name} < 0.1.5-12
Obsoletes:  python2-%{pypi_name} < 0.1.5-12

%description -n python3-%{pypi_name}
This is MultipartPostHandler plus a fix for UTF-8 systems.
Enables the use of multipart/form-data for posting forms.

%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf doc # no real doc there

find . -name '*.py' | xargs sed -i '1s|^#!%{__python}|#!%{__python3}|'
2to3 --write --nobackup *.py examples/*.py
%patch1 -p1

# also change the URL in the Py2 example
sed -i 's|http://www.google.com|https://getfedora.org/|' examples/MultipartPostHandler-example.py

%build
%py3_build

%install
%py3_install

%if %{with internet}
%check
# do it form a different folder
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} examples/MultipartPostHandler-example.py > py3.html
%endif # with internet

%files -n python3-%{pypi_name}
%doc README.txt examples/MultipartPostHandler-example.py
%{python3_sitelib}/MultipartPostHandler*
%{python3_sitelib}/__pycache__/MultipartPostHandler*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-20
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-17
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-13
- Rebuilt for Python 3.7

* Wed Mar 28 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-12
- Remove the python2 subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.5-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)
- BR %%{_bindir}/2to3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-7
- Rebuild for Python 3.6

* Tue Nov 15 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-6
- Modernize the spec
- Make the %%check pass
- Do not own the __pycache__ directory

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 25 2014 Sérgio Basto <sergio@serjux.com> - 0.1.5-1
- Update to 0.1.5
- Removed upstreamed patch.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 02 2014 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-6
- Rebuilt for Python 3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 22 2013 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-4
- Dealing with more Pyhton 3 stuff

* Thu Mar 21 2013 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-3
- Remove the example in main() from the library and keep it separated
- Added patch witch Python 3 specific things

* Wed Feb 20 2013 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-2
- Introduced Python 3 subpackage

* Fri Jan 25 2013 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-1
- Created by pyp2rpm-0.5.1
- Revised

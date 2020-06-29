%if ! (0%{?fedora} || 0%{?rhel} > 5)
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif

%if 0%{?fedora} || 0%{?suse_version} > 1320
%global build_py3   1
%endif

Summary: Streaming zlib (gzip) support for python
Name: python-gzipstream
Version: 2.8.6
Release: 10%{?dist}
URL:        https://github.com/spacewalkproject/spacewalk/wiki/Projects_python-gzipstream
Source0:    https://github.com/spacewalkproject/spacewalk/archive/python-gzipstream-%{version}.tar.gz
License: GPLv2
BuildArch: noarch


%global _description\
A streaming gzip handler.\
gzipstream.GzipStream extends the functionality of the gzip.GzipFile class\
to allow the processing of streaming data.\


%description %_description

%if 0%{?build_py3}
%package -n python3-gzipstream
Summary:        %summary
BuildRequires:  python3-devel

%description -n python3-gzipstream %_description

%endif

%prep
%setup -q
mkdir ../py3
cp -a . ../py3

%build
%if 0%{?build_py3}
cd ../py3
%{__python3} setup.py build

%endif

%install
%if 0%{?build_py3}
cd ../py3
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --prefix %{_usr}

%endif

%if 0%{?build_py3}
%files -n python3-gzipstream
%{python3_sitelib}/*
%doc html
%license LICENSE

%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.8.6-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.8.6-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.8.6-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Miro Hrončok <mhroncok@redhat.com> - 2.8.6-4
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.8.6-2
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Tomas Kasparek <tkasparek@redhat.com> 2.8.6-1
- mark license for python3 subpackage
- remove empty section
- Update Python 2 dependency declarations to new packaging standards

* Fri Feb 09 2018 Michael Mraka <michael.mraka@redhat.com> 2.8.5-1
- removed %%%%defattr from specfile
- removed Group from specfile

* Wed Nov 08 2017 Jan Dobes 2.8.4-1
- raise exception instead of returning
- fix syntax for python3
- build python3 subpackage

* Wed Sep 06 2017 Michael Mraka <michael.mraka@redhat.com> 2.8.3-1
- purged changelog entries for Spacewalk 2.0 and older

* Fri Sep 01 2017 Jan Dobes 2.8.2-1
- rebuild package in Koji (rhel 7 buildroot was missing macros and python-gzipstream obsolete wasn't added)

* Thu Aug 31 2017 Jan Dobes 2.8.1-1
- in master we are on 2.8 already

* Mon Aug 21 2017 Miroslav Suchý <msuchy@redhat.com> 2.7.2-1
- modernize spec
- rename python-gzipstream to python2-gzipstream
- Bumping package versions for 2.8.

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.7.1-2
- Python 2 binary package renamed to python2-gzipstream
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Mon Jul 17 2017 Jan Dobes 2.7.1-1
- Updated links to github in spec files
- Migrating Fedorahosted to GitHub
- Bumping package versions for 2.7.
- Bumping package versions for 2.6.
- Bumping package versions for 2.5.
- Bumping package versions for 2.4.

* Thu Mar 19 2015 Grant Gainey 2.3.3-1
- Updating copyright info for 2015

* Thu Feb 05 2015 Stephen Herr <sherr@redhat.com> 2.3.2-1
- Relicense python-gzipstream to be GPL only

* Thu Jan 15 2015 Matej Kollar <mkollar@redhat.com> 2.3.1-1
- Getting rid of Tabs and trailing spaces in LICENSE, COPYING, and README files
- Bumping package versions for 2.3.
- Bumping package versions for 2.2.


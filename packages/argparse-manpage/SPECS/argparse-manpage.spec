%if 0%{?fedora}
  %bcond_without python3
  %if 0%{?fedora} > 29
    %bcond_with python2
  %else
    %bcond_without python2
  %endif
%else
  %if 0%{?rhel} > 7
    %bcond_with    python2
    %bcond_without python3
  %else
    %bcond_without python2
    %bcond_with    python3
  %endif
%endif

%bcond_without check


%global sum()   Build manual page from %* ArgumentParser object
%global desc \
Generate manual page an automatic way from ArgumentParser object, so the \
manpage 1:1 corresponds to the automatically generated --help output.  The \
manpage generator needs to known the location of the object, user can \
specify that by (a) the module name or corresponding python filename and \
(b) the object name or the function name which returns the object. \
There is a limited support for (deprecated) optparse objects, too.


Name:           argparse-manpage
Version:        1.2.2
Release:        1%{?dist}
Summary:        %{sum Python}
BuildArch:      noarch

License:        ASL 2.0
URL:            https://github.com/praiskup/%{name}
Source0:        %pypi_source

%if %{with python2}
BuildRequires: python2-setuptools python2-devel
%if %{with check}
%if 0%{?rhel} && 0%{?rhel} == 7
BuildRequires: pytest python-six
%else
BuildRequires: python2-pytest python2-six
%endif
%endif
%endif
%if %{with python3}
BuildRequires: python3-setuptools python3-devel
%if %{with check}
BuildRequires: python3-pytest python3-six
%endif
%endif
%if %{with python3}
Requires: python3-%name = %version-%release
%else
Requires: python2-%name = %version-%release
%endif

%description
%desc


%package -n     python2-%name
Summary:        %{sum Python 2}

%description -n python2-%name
%{desc}


%package -n     python3-%name
Summary:        %{sum Python 3}

%description -n python3-%name
%{desc}


%prep
%setup -q


%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif


%install
%if %{with python2}
%py2_install
%endif
%if %{with python3}
%py3_install
%endif



%if %{with check}
%check
%if %{with python2}
PYTHONPATH=%buildroot%python2_sitearch %__python2 -m pytest
%endif
%if %{with python3}
PYTHONPATH=%buildroot%python3_sitearch %__python3 -m pytest
%endif
%endif


%files
%license LICENSE
%{_bindir}/argparse-manpage
%_mandir/man1/argparse-manpage.1.*
%if %{with python3}
%python3_sitelib/build_manpages/cli
%else
%python2_sitelib/build_manpages/cli
%endif


%if %{with python2}
%files -n python2-%name
%license LICENSE
%python2_sitelib/build_manpages
%python2_sitelib/argparse_manpage-%{version}*.egg-info
%exclude %python2_sitelib/build_manpages/cli
%endif


%if %{with python3}
%files -n python3-%name
%license LICENSE
%python3_sitelib/build_manpages
%python3_sitelib/argparse_manpage-%{version}*.egg-info
%exclude %python3_sitelib/build_manpages/cli
%endif


%changelog
* Sat Sep 07 2019 Pavel Raiskup <praiskup@redhat.com> - 1.2.2-1
- new release

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-6
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Pavel Raiskup <praiskup@redhat.com> - 1.1-3
- drop python3 on F30+ (rhbz#1634992)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Pavel Raiskup <praiskup@redhat.com> - 1.1-1
- v1.1

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.7

* Mon Feb 19 2018 Pavel Raiskup <praiskup@redhat.com> - 1.0.0-1
- initial RPM packaging

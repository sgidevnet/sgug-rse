%global pkg ctable

Name:           emacs-%{pkg}
Version:        0.1.2
Release:        1%{?dist}
Summary:        Table Component for Emacs Lisp

License:        GPLv3+
URL:            https://github.com/kiwanami/%{name}/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  emacs
Requires:       emacs(bin) >= %{_emacs_version}
BuildArch:      noarch

%description
ctable.el is a table component for emacs lisp. Emacs lisp programs can display a
nice table view from an abstract data model. The many emacs programs have the
code for displaying table views, such as dired, list-process, buffer-list and so
on. So, ctable.el would provide functions and a table framework for the table
views.


%prep
%autosetup


%build
%{_emacs_bytecompile} %{pkg}.el


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 *.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/


%files
%doc readme.md
%{_emacs_sitelispdir}/%{pkg}/


%changelog
* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.1.2-1
- Initial RPM release

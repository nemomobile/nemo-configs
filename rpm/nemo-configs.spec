Name:		nemo-configs
Version:	0
Release:	1
Summary:	Configuration for different parts of nemo

Group:		Configs
License:	GPLv2
URL:		https://github.com/nemomobile/nemo-configs
Source0:	%{name}-%{version}.tar.bz2

%description
%{summary}

%package connman
Group:  Configs
Summary: Connman configs for nemo
Provides: connman-configs
Conflicts: connman-configs-mer

%description connman
%{summary}

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files connman
%defattr(-,root,root,-)
%config %{_sysconfdir}/connman/main.conf

